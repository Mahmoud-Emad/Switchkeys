# SwitchKeys Dart Client

This guide provides step-by-step instructions on how to install and use the SwitchKeys Dart client to manage users, organizations, projects, environments, and user features.

## Installation

To install the SwitchKeys Dart client, add it as a dependency to your Dart project's `pubspec.yaml` file:

```yaml
dependencies:
  switchkeys: ^1.1.5
```

Then, run the following command in your terminal to fetch the package:

```bash
dart pub get
```

## Usage

Here's a basic example of how to use the SwitchKeys TS Client:

```dart
// This Dart script demonstrates how to use the SwitchKeys authentication API.

import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeys
final SwitchKeys switchkeys = SwitchKeys();

try {
  // If you haven't created account yet, unlock the register method.
  var user = await switchkeys.auth.register(
    firstName: "Testing",
    lastName: "Account",
    email: "testing@switchkeys.com",
    password: "0000",
    memberType: UserTypeEnum.administrator,
  );
  print("[+] Registered successfully: ${user.email}");
} catch (e) {
  var user = await switchkeys.auth.login(
    email: "testing@switchkeys.com",
    password: "0000",
  );
  print("[+] Logged in successfully: ${user.email}");
} finally {
  switchkeys.auth.logout();
  print("[+] Logged out successfully");
}

```

For more detailed usage instructions, refer to the [examples folder](https://github.com/Mahmoud-Emad/Switchkeys/tree/development/clients/dart/switchkeys/lib/examples).

## Organization Management

The SwitchKeys Dart Client allows you to manage organizations within the SwitchKeys system. Here are some examples of organization-related operations:

### Creating an Organization

```dart
// ------------------------------------------------------------------------
// Creating a new organization
// ------------------------------------------------------------------------
// Create a new organization named "SwitchKeys".
var organization = await switchkeys.organizations.create(
  name: "SwitchKeys",
);
print("[+] Created organization name: ${organization.name}");

```

Before using the SwitchKeys Dart Client, make sure to set up the necessary environment variables and configuration files. Refer to the [configuration documentation](https://github.com/Mahmoud-Emad/Switchkeys/blob/development/clients/dart/switchkeys/docs/configuration.md) for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/Mahmoud-Emad/Switchkeys/blob/development/clients/dart/switchkeys/LICENSE)
