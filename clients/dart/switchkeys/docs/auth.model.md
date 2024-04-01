# Usage Documentation for SwitchKeys Authentication API

## Overview

This Dart script demonstrates how to use the SwitchKeys authentication API. It includes examples of logging in an existing user and registering a new user, along with error handling for both processes.

## Logging in an Existing User

To log in an existing user, use the `login` method provided by the `SwitchKeyAuth` class. Provide the user's email and password as parameters. If the login is successful, the user's email will be printed. If an error occurs during the login process, the error message will be printed.

Example:

```dart

import 'package:switchkeys/src/api/models/auth.dart';
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeyAuth
SwitchKeyAuth auth = SwitchKeys.auth();

// Now you can use the auth instance to make API calls
// Logging in an existing user
await auth
    .login(email: "hamada__2020@gmail.com", password: "hamada")
    .then((user) => print("Logged in successfully: ${user.email}"))
    .catchError((e) => print("Error logging in: $e"));
```

## Registering a New User

To register a new user, use the `register` method provided by the `SwitchKeyAuth` class. Provide the user's first name, last name, email, password, and user type (optional) as parameters. If the registration is successful, the user's email will be printed. If an error occurs during the registration process, the error message will be printed.

Example:

```dart

import 'package:switchkeys/src/api/models/auth.dart';
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeyAuth
SwitchKeyAuth auth = SwitchKeys.auth();

// Now you can use the auth instance to make API calls
// Registering a new user

await auth
    .register(
      firstName: "Ahmed",
      lastName: "Zain",
      email: "hamada__2020@gmail.com",
      password: "hamada",
      userType: UserTypeEnum.administrator,
    )
    .then((user) => print("User registered successfully: ${user.email}"))
    .catchError((e) => print("Error registering user: $e"));
```

## Conclusion

By following these usage examples, you can effectively utilize the SwitchKeys authentication API in your Dart applications to log in existing users and register new users, while handling errors gracefully.
