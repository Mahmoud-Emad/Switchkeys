# SwitchKeys Dart Client

This guide provides step-by-step instructions on how to install and use the SwitchKeys Dart client to manage users, organizations, projects, environments, and user features.

## Installation

To install the SwitchKeys Dart client, add it as a dependency to your Dart project's `pubspec.yaml` file:

```yaml
dependencies:
  switchkeys: ^1.0.0
```

Then, run the following command in your terminal to fetch the package:

```bash
dart pub get
```

## User Registration and Login

### Registering a New User

To register a new user, use the `register` method provided by the `SwitchKeyAuth` class. Provide the user's first name, last name, email, password, and user type (optional) as parameters:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeyAuth
SwitchKeys switchKeys = SwitchKeys();

// Register a new user
await switchKeys.auth.register(
  firstName: "John",
  lastName: "Doe",
  email: "john@example.com",
  password: "password",
);
```

### Logging in an Existing User

To log in an existing user, use the `login` method provided by the `SwitchKeyAuth` class. Provide the user's email and password as parameters:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeyAuth
SwitchKeys switchKeys = SwitchKeys();

// Log in an existing user
await switchKeys.auth.login(
  email: "john@example.com",
  password: "password",
);
```

## Managing Organizations and Projects

### Creating an Organization

To create a new organization, use the `create` method provided by the `SwitchKeysOrganizations` class:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeysOrganizations
SwitchKeys switchKeys = SwitchKeys();

// Create a new organization
await switchKeys.organizations.create(name: "My Organization");
```

### Creating a Project

To create a new project within an organization, use the `create` method provided by the `SwitchKeysProjects` class:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeysProjects
SwitchKeys switchKeys = SwitchKeys();

// Create a new project within an organization
await switchKeys.projects.create(name: "My Project", organizationId: 1);
```

## Managing Environments and User Features

### Creating an Environment

To create a new environment, use the `create` method provided by the `SwitchKeysEnvironments` class:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeysEnvironments
SwitchKeys switchKeys = SwitchKeys();

// Create a new environment
await switchKeys.environments.create(name: "Production", projectId: 1);
```

### Adding Users to an Environment

To add users to an environment, use the `addUser` method provided by the `SwitchKeysEnvironments` class:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeysEnvironments
SwitchKeys switchKeys = SwitchKeys();

// Add a user to an environment
await switchKeys.environments.users.addUser(
  user: SwitchKeysEnvironmentsUser(username: "user1"),
  environmentKey: "0246204d-c567-4089-add2-a1155657ecac", // Environment key
);
```

### Setting User Features in an Environment

To set user features in an environment, use the `addFeature` method provided by the `SwitchKeysEnvironmentsUsers` class:

```dart
import 'package:switchkeys/src/core/base.dart';

// Get an instance of SwitchKeysEnvironmentsUsers
SwitchKeys switchKeys = SwitchKeys();

// Set user features in an environment
await switchKeys.environments.users.addFeature(
  username: "user1",
  feature: SwitchKeyUserEnvironmentFeatures(name: "Feature1", value: "Value1"),
  environmentKey: "0246204d-c567-4089-add2-a1155657ecac", // Environment key
);
```

---

Follow these steps to install the SwitchKeys Dart client and perform various actions such as registering/logging in a user, creating an organization, creating a project within the organization, creating an environment, adding users to the environment, and setting user features within the environment.
