# SwitchKeys TS Client

The SwitchKeys TS Client is a TypeScript client library for interacting with the SwitchKeys system. It provides convenient methods for user authentication, user management, and other operations within the SwitchKeys ecosystem.

## Features

- **User Authentication**: Register new users, log in to existing users, and manage user tokens.
- **User Management**: Retrieve user information by ID or email, create new users, update existing users, and delete users.
- **Configuration Management**: Load, check, and write configuration settings, including user tokens.

## Installation

You can install the SwitchKeys TS Client via npm:

```bash
npm install switchkeys-ts-client
```

## Usage

Here's a basic example of how to use the SwitchKeys TS Client:

```typescript
import SwitchKeys from "switchkeys-ts-client";

async function main() {
  const switchkeys = new SwitchKeys();

  // Register a new user
  const newUser = await switchkeys.auth.register({
    email: "user@example.com",
    firstName: "John",
    lastName: "Doe",
    password: "password",
  });
  console.log(`New user registered. Access token: ${newUser.accessToken}`);

  // Log in an existing user
  const loggedInUser = await switchkeys.auth.login({
    email: "user@example.com",
    password: "password",
  });
  console.log(`User logged in. Access token: ${loggedInUser.accessToken}`);

  // Retrieve user data by ID
  const userByID = await switchkeys.users.getByID(1);
  console.log(`User data retrieved by ID. First name: ${userByID.firstName}`);

  // Retrieve user data by email
  const userByEmail = await switchkeys.users.getByEmail("user@example.com");
  console.log(`User data retrieved by email. First name: ${userByEmail.firstName}`);
}

main();
```

For more detailed usage instructions, refer to the [documentation](link-to-docs).

## Configuration

Before using the SwitchKeys TS Client, make sure to set up the necessary environment variables and configuration files. Refer to the [configuration documentation](link-to-config-docs) for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](link-to-license).
