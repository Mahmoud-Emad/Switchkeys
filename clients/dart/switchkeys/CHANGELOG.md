# SwitchKeys Changelog

## Version 1.0.7

### Features

- Added a new feature to create three different environments when creating a new project:
  - Development
  - Staging
  - Production

### Usage

Now, when creating a new project, you can access the environment keys based on their names. For example:

```dart
print("Project 1 development environment key: ${project.environments.development.environmentKey}.");
```
