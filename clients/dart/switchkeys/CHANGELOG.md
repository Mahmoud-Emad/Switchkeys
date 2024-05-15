# SwitchKeys Changelog

## Version 1.0.8

### 1.0.8 Features

- Updated the request/response of adding/getting user features
- Commented un-needed caller for now
- Added missing fields in the backend
- Fixed the README.md with the newly added changes
- Fixed the dart example
- Removed dead-code
- Added print, to print the result coming from the server

### 1.0.8 Usage

Now, when creating a new project, you can access the environment keys based on their names. For example:

```dart
print("Project 1 development environment key: ${project.environments.development.environmentKey}.");
```

## Version 1.0.6

### 1.0.6 Features

- Added a new feature to create three different environments when creating a new project:
  - Development
  - Staging
  - Production

### Usage

Now, when creating a new project, you can access the environment keys based on their names. For example:

```dart
print("Project 1 development environment key: ${project.environments.development.environmentKey}.");
```
