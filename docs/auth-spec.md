# Authentication Specification

## Purpose

This document defines the required authentication behavior of the
platform.

Responsibilities

* Define authentication workflows
* Define security requirements
* Define recovery behavior
* Define session behavior
* Define trust-level behavior

This document specifies how authentication must behave regardless of the
implementation.

It is independent of implementation details and changes only when the
authentication requirements change.

## Core Principle

No password field anywhere in the user model.

## Token Architecture

* Access token: JWT, signed (RS256/ES256), 5-15min expiry, httpOnly 
  + Secure + SameSite=Strict cookie. Verified by signature/expiry 
  only — no DB lookup, fully stateless. Accept that a stolen token 
  remains valid until natural expiry; this is a bounded-risk 
  tradeoff, not a closed hole — keep the window short rather than 
  adding a blacklist.
* Refresh token: JWT, longer-lived, same cookie flags, carries a 
  `token_version` claim checked against a stored integer per user 
  (or per device, for individual-device revocation). This is the 
  one deliberate point of statefulness — a single integer compare 
  on refresh, not a token blacklist table.
* Refresh token ROTATION: issue a new refresh token on every use, 
  invalidate the prior one. If an already-rotated (superseded) 
  refresh token is ever presented again, treat it as theft 
  evidence — kill the whole session chain (bump token_version) 
  immediately. This is what catches stolen-refresh-token replay 
  without needing a blacklist.
* CSRF protection: separate non-httpOnly token (double-submit or 
  custom-header pattern) required on all state-changing requests, 
  since SameSite=Strict alone narrows but doesn't fully eliminate 
  cross-site request risk.
* "Log out all devices" = bump token_version. "Log out this 
  device" = per-device version/row if tracking individually.

1. REGISTRATION / ENTRY
   * Single screen offers: [Email] or [Continue with Google] or 
     [Continue with Apple].
   * Email path: submit email → OTP code sent (6-digit, typed in 
     same view, no separate magic-link page) → 5min expiry, 5 
     attempt limit, then must re-request.
   * OAuth path: standard OIDC redirect → verify email_verified 
     == true → match against existing account by verified email 
     or provider `sub`; create account if new.
   * Successful verification (either path) creates the account 
     and authenticates the session.

2. PASSKEY ENROLLMENT (immediately after first successful login)
   * Prompt: "Secure your account — set up a passkey." Optional, 
     not blocking.
   * Standard WebAuthn ceremony (navigator.credentials.create()); 
     let browser/OS decide local biometric vs. QR/hybrid-to-phone 
     automatically — do not hardcode a method.
   * Support multiple passkeys per account (phone + laptop, etc.). 
     After first passkey, soft-nudge: "Add this on another device 
     too" — optional, zero-friction resilience.
   * If declined or unsupported: continue with email-OTP login.

3. DAY-TO-DAY LOGIN
   * Passkey is primary if registered (inherently MFA — possession 
     + biometric in one ceremony, no separate 2FA/OTP layered on 
     top).
   * Email-OTP and Google/Apple sign-in remain available as equal, 
     visible parallel options — never hidden as degraded fallbacks.

4. SENSITIVE-ACTION GATE
   * Require a FRESH passkey assertion at the moment of the 
     sensitive action itself (re-prompt biometric), not a static 
     "has passkey on file" flag checked once at login. This is 
     what stops an email-OTP-only authenticated session from 
     reaching sensitive actions even if the account has a passkey 
     registered elsewhere.
   * Also require a verified backup channel on file (backup email 
     or linked OAuth), linked only while already authenticated.

5. ACCOUNT RECOVERY (tiered, escalating)
   * Tier 1: Lost passkey, primary email/OAuth still accessible → 
     re-authenticate via email-OTP or linked OAuth → register new 
     passkey on current device.
   * Tier 2: Primary email/OAuth also lost → authenticate via 
     backup email (OTP) → re-link/re-register as above. Apply 
     risk-based step-up (new device/IP/geo) and notify all other 
     registered channels that a recovery event occurred.
   * Tier 3: Total lockout (all channels lost) → identity 
     verification (government ID + biometric liveness, via KYC 
     vendor) → cooling-off period (24–72h) before new credential 
     activates. Can launch as manual/support-assisted at v1, 
     automate later once lockout volume justifies it.

6. ACCOUNT SETTINGS (ongoing)
   * List of registered passkeys/devices, with add/revoke.
   * "Log out all devices" / revoke-all-sessions control.
   * Backup email and linked OAuth identities manageable here.

## Security Notes

* Email-OTP-only sessions (no passkey activated) are accepted as a 
  lower-trust tier — fine for read-only/low-risk actions, blocked 
  from sensitive actions by the gate in (4). Security posture 
  depends on that gate being a live check, not a flag.
* httpOnly blocks JS/XSS-based token theft specifically — it does 
  not hide tokens from DevTools or a compromised machine. Defense 
  is layered: httpOnly (XSS) + Secure/HTTPS (network) + SameSite 
  (CSRF) + short expiry (bounds any other leak) + rotation/reuse 
  detection (catches refresh-token theft after the fact).