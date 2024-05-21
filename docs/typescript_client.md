# SwitchKeys TS Client

The SwitchKeys TS Client is a TypeScript client library for interacting with the SwitchKeys system.
It provides convenient methods for `User authentication`, `Organization Management`, `Project Management`, and other operations within the SwitchKeys system.

## Features

- **User Authentication**: Register new users, log in to existing users, and manage user tokens.
- **Organization Management**: Create, retrieve, update, and delete organizations. Add and remove members from organizations.
- **Project Management**: Create, retrieve, update, and delete projects.
- **Environment Management**: Create, retrieve, update, and delete environments.

## Installation

You can install the SwitchKeys TS Client via npm:

```bash
npm install @switchkeys/ts-client
# or
yarn add @switchkeys/ts-client
```

## Usage

Here's a basic example of how to use the SwitchKeys TS Client:

```typescript
// Import the SwitchKeys class from the client library.
import SwitchKeys, { DeviceTypeSelection } from "@switchkeys/ts-client";

export async function main() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  await switchkeys.auth.login({
    email: "user@example.com",
    password: "###",
  });

  console.log("Logged in successfully.");
}

main();
```

For more detailed usage instructions, refer to the [examples folder](.././examples/).

## Organization Management

The SwitchKeys TS Client allows you to manage organizations within the SwitchKeys system. Here are some examples of organization-related operations:

### Creating an Organization

```typescript
const organization = await switchkeys.organizations.create({ name: "Test Organization" });
console.log(`Organization created. ID: ${organization.id}`);
```

## Configuration

Before using the SwitchKeys TS Client, make sure to set up the necessary environment variables and configuration files. Refer to the [configuration documentation](./docs/configuration.md) for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](.././LICENSE)
