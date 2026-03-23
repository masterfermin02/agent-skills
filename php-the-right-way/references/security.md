# PHP Security — The Right Way

Source: https://phptherightway.com

## SQL Injection — Always Use Prepared Statements

```php
// NEVER DO THIS
$query = "SELECT * FROM users WHERE email = '$email'";

// CORRECT — PDO with prepared statements
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute([':email' => $email]);
$user = $stmt->fetch();

// CORRECT — MySQLi
$stmt = $mysqli->prepare('SELECT * FROM users WHERE email = ?');
$stmt->bind_param('s', $email);
$stmt->execute();
```

## XSS — Always Escape Output

```php
// NEVER echo raw user input
echo $_GET['name'];

// ALWAYS escape before output
echo htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8');

// Helper function
function e(string $value): string {
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
```

## Password Hashing — Never MD5/SHA1

```php
// NEVER
$hash = md5($password);    // broken
$hash = sha1($password);   // broken

// CORRECT
$hash = password_hash($password, PASSWORD_BCRYPT);
// or
$hash = password_hash($password, PASSWORD_ARGON2ID); // preferred PHP 7.3+

// Verify
if (password_verify($inputPassword, $storedHash)) {
    // authenticated
}

// Rehash check (after algorithm upgrade)
if (password_needs_rehash($hash, PASSWORD_ARGON2ID)) {
    $hash = password_hash($password, PASSWORD_ARGON2ID);
    // update stored hash
}
```

## CSRF Protection

```php
// Generate token
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

// In form
echo '<input type="hidden" name="csrf_token" value="' . $_SESSION['csrf_token'] . '">';

// On submit — validate
if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'] ?? '')) {
    http_response_code(403);
    exit('CSRF validation failed');
}
```

## Session Security

```php
session_start();

// Regenerate ID on privilege change (login, logout)
session_regenerate_id(true);

// Secure session config (php.ini or runtime)
ini_set('session.cookie_httponly', '1');
ini_set('session.cookie_secure', '1');   // HTTPS only
ini_set('session.cookie_samesite', 'Strict');
ini_set('session.use_strict_mode', '1');
```

## Input Filtering

```php
// Filter specific types
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$age   = filter_input(INPUT_POST, 'age', FILTER_VALIDATE_INT);
$url   = filter_input(INPUT_GET, 'redirect', FILTER_VALIDATE_URL);

if ($email === false || $email === null) {
    // invalid or missing
}

// Sanitize (strip dangerous chars)
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_SPECIAL_CHARS);
```

## File Uploads

```php
// Validate MIME type — never trust $_FILES['type']
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file($_FILES['upload']['tmp_name']);

$allowed = ['image/jpeg', 'image/png', 'image/gif'];
if (!in_array($mimeType, $allowed, true)) {
    throw new \InvalidArgumentException('Invalid file type');
}

// Store outside web root or use random filename
$filename = bin2hex(random_bytes(16)) . '.jpg';
move_uploaded_file($_FILES['upload']['tmp_name'], '/storage/' . $filename);
```

## Data Encryption

```php
// Use libsodium (built into PHP 7.2+)
$key = sodium_crypto_secretbox_keygen();
$nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);

$encrypted = sodium_crypto_secretbox($plaintext, $nonce, $key);
$decrypted = sodium_crypto_secretbox_open($encrypted, $nonce, $key);
```

Never use `mcrypt` (removed in PHP 7.2) or `openssl_encrypt` without proper key management.
