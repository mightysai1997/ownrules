
// ------------------------------
// ⚠️ HARD-CODED API SECRETS
// ------------------------------

// Stripe secret key (should be in env variable)
const stripeSecret = "sk_live_1234567890abcdefABCDEF";

// GitHub token (should be in secret manager)
const githubToken = "ghp_abcdEFGHIJKLmnopQRSTUVwxYZ123456789";

// JWT string in variable (starts with 'eyJ')
const jwtToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abcd.def";

// Secret in config
const config = {
  access_token: "abc.def.ghi123",
  secret_key: "sk_test_abcdef1234567890"
};

// ------------------------------
// ⚠️ TOKENS IN URL
// ------------------------------

const url1 = "https://api.example.com/user?token=abc123def456";
const url2 = "https://secure.site/data?access_token=XYZ987654321";
fetch("https://myapp.com/resource?auth=abcd1234xyz");

// ------------------------------
// ⚠️ HARDCODED JWT SECRET USING JOSE
// ------------------------------

const { JWT, JWK } = require("jose");

// Signing with hardcoded secret
const signed = JWT.sign({ user: "admin" }, "hardcoded-secret", {
  algorithm: "HS256"
});

// Verifying with hardcoded secret
const verified = JWT.verify(signed, "hardcoded-secret", {
  algorithms: ["HS256"]
});

// Signing with hardcoded JWK
const jwkKey = JWK.asKey("jwk-hardcoded-key");
const signedWithJWK = JWT.sign({ role: "user" }, jwkKey);
