# Usage Documentation for SwitchKeys Authentication API

## Overview

This Dart script demonstrates how to use the SwitchKeys authentication API. It includes examples of logging in an existing user and registering a new user, along with error handling for both processes.

## Logging in an Existing User

To log in an existing user, use the `login` method provided by the `SwitchKeyAuth` class. Provide the user's email and password as parameters. If the login is successful, the user's email will be printed. If an error occurs during the login process, the error message will be printed.

Example:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeyAuth
SwitchKeys switchKeys = SwitchKeys();

// Now you can use the auth instance to make API calls
// Logging in an existing user
var user = await switchkeys.auth.login(
  email: "testing@switchkeys.com",
  password: "0000",
);
print("[+] Logged in successfully: ${user.email}");


```

## Registering a New User

To register a new user, use the `register` method provided by the `SwitchKeyAuth` class. Provide the user's first name, last name, email, password, and user type (optional) as parameters. If the registration is successful, the user's email will be printed. If an error occurs during the registration process, the error message will be printed.

Example:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeyAuth
SwitchKeys switchKeys = SwitchKeys();

// Now you can use the auth instance to make API calls
var user = await switchkeys.auth.register(
  firstName: "Testing",
  lastName: "Account",
  email: "testing@switchkeys.com",
  password: "0000",
  memberType: UserTypeEnum.administrator,
);
print("[+] Registered successfully: ${user.email}");
```
