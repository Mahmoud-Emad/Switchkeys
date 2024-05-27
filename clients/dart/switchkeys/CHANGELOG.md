# SwitchKeys Changelog

## Version 1.1.4

## What's Changed (1.1.4)

* feat: Added TS example runner. by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/29>

**Full Changelog**: <https://github.com/Mahmoud-Emad/Switchkeys/compare/v1.0.3...v1.0.4>

## Version 1.1.0

## What's Changed (1.1.0)

* Updated the TSClient with some bug fixes and features by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/16>
* Development backend v0.2.0 by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/15>
* fix: Updated the backend with missing implementations: by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/17>
* fix: Updated the response of Adding/Removing organization members: by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/18>
* fix: Added logs in the zinit runserver service. by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/20>
* Development backend v0.2.3 by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/21>
* fix: Fixed an issue with building the backend container. by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/22>
* Development ts client v4.5 by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/23>
* Updated the update feature serializer class name. by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/24>
* Development ts client v4.6 by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/25>
* Added missing '@types/uuid-validate' package. by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/27>
* fix: Updated the response of setting a feature for a user, changed the Serializer class. by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/28>
* Development dart client v1.0.9 by @Mahmoud-Emad in <https://github.com/Mahmoud-Emad/Switchkeys/pull/19>

**Full Changelog**: <https://github.com/Mahmoud-Emad/Switchkeys/compare/v1.0.1...v1.0.2>

## Version 1.0.8

### What's Changed (1.0.8)

* Updated the request/response of adding/getting user features
* Commented un-needed caller for now
* Added missing fields in the backend
* Fixed the README.md with the newly added changes
* Fixed the dart example
* Removed dead-code
* Added print, to print the result coming from the server

### 1.0.8 Usage

Now, when creating a new project, you can access the environment keys based on their names. For example:

```dart
print("Project 1 development environment key: ${project.environments.development.environmentKey}.");
```

## Version 1.0.6

### 1.0.6 Features

* Added a new feature to create three different environments when creating a new project:
  * Development
  * Staging
  * Production

### Usage

Now, when creating a new project, you can access the environment keys based on their names. For example:

```dart
print("Project 1 development environment key: ${project.environments.development.environmentKey}.");
```
