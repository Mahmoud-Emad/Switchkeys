// Import the SwitchKeys class from the client library.
import SwitchKeys from "../src/core/base";
import { DeviceTypeSelection, SwitchKeysUserType } from "../src/utils/types";

/**
 * `environmentExample` demonstrates the usage of environment services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys environment, including loading an environment, adding users,
 * and managing features.
 */
export async function environmentExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();
  const userEmail = "testing@switchkeys.com";

  // --------------------------------------------------------------------------------------------------------------------
  // Check if the user is already created
  // --------------------------------------------------------------------------------------------------------------------
  console.log(`[+] Check if user with email ${userEmail} is registered.`);
  const userCreated = await switchkeys.users.isUserCreated({
    email: userEmail,
  });

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  if (!userCreated) {
    // If you haven't created account yet, unlock the register method.
    await switchkeys.auth.register({
      email: userEmail,
      password: "0000",
      firstName: "Testing",
      lastName: "Account",
      memberType: SwitchKeysUserType.Administrator,
    });
    console.log("[+] Registered successfully.");
  } else {
    console.log(`[!] User with email ${userEmail} is already registered.`);
    await switchkeys.auth.login({
      email: userEmail,
      password: "0000",
    });
    console.log("[+] Logged in successfully.");

    // --------------------------------------------------------------------------------------------------------------------
    // Creating a New Organization
    // --------------------------------------------------------------------------------------------------------------------
    // Second, create a new organization.
    const organization = await switchkeys.organizations.create({
      name: "SwitchKeys7",
    });

    // --------------------------------------------------------------------------------------------------------------------
    // Creating a New Project within the Organization
    // --------------------------------------------------------------------------------------------------------------------
    // After creating the organization, create a project within it.
    const project = await organization.createProject({
      name: "StoryMith",
    });

    // --------------------------------------------------------------------------------------------------------------------
    // Loading an Environment from the Created Project
    // --------------------------------------------------------------------------------------------------------------------
    // Every created project comes with three different types of environments ['development', 'staging', 'production'].
    // Every environment has its name and key.
    const environmentKey = project.environments.development.environmentKey;

    // Load the environment using the environment key.
    const environment = await switchkeys.environments.load(environmentKey);
    console.log("[+] Loaded Environment:", environment);

    const debugFeatureName = "debug";

    // --------------------------------------------------------------------------------------------------------------------
    // Adding a User to the Environment
    // --------------------------------------------------------------------------------------------------------------------
    // Add a user to the environment.
    const username1 = "user1";
    await environment.addUser({
      device: {
        deviceType: DeviceTypeSelection.ANDROID,
        version: "v15s.521.s",
      },
      username: username1,
    });

    console.log(`[+] Added user: ${username1}`, {
      user1Features: environment.users.get(username1)?.features,
    });

    // --------------------------------------------------------------------------------------------------------------------
    // Managing Features in the Environment
    // --------------------------------------------------------------------------------------------------------------------
    // Check if the environment has the "debug" feature.
    if (environment.hasFeature(debugFeatureName)) {
      const debugFeature = environment.getFeature(debugFeatureName);

      if (debugFeature) {
        // Toggle the "debug" feature value.
        const newValue = debugFeature.value === "true" ? "false" : "true";
        const updatedFeature = await environment.updateFeature({
          name: debugFeatureName,
          newName: debugFeatureName,
          newValue: newValue,
        });

        console.log("[+] Updated Feature:", updatedFeature);
      }
    } else {
      // Add the "debug" feature if it does not exist.
      const newFeature = await environment.addFeature({
        name: debugFeatureName,
        value: "false",
      });

      console.log("[+] Added Feature:", newFeature);

      // Update the added feature.
      const updatedFeature = await environment.updateFeature({
        name: debugFeatureName,
        newName: debugFeatureName,
        newValue: "true",
      });

      console.log("[+] updated Feature:", updatedFeature);
    }

    // Verify that the new feature is added to user1.
    console.log("[+] User1 Features after adding 'debug':", {
      user1Features: environment.users.get(username1)?.features,
    });

    // Check and add a feature for any user inside the environment with a different value.
    const envUser = environment.users.get(username1);
    const featureName = "theme";
    if (envUser.hasFeature(featureName)) {
      console.log(
        `[+] User has the '${envUser.getFeature(featureName).name}' feature, the value is: '${envUser.getFeature(featureName).value}'.`
      );
    } else {
      await envUser.setFeature({
        name: featureName,
        value: "dark"
      })
      console.log(`[+] Feature ${featureName} has been added to the user, th value is '${envUser.getFeature(featureName).value}'.`)
    }

    // --------------------------------------------------------------------------------------------------------------------
    // Deleting the Created Organization
    // --------------------------------------------------------------------------------------------------------------------
    // This will also delete all associated projects and environments.
    await switchkeys.organizations.delete(organization.id);

    console.log(
      "[+] Deleted organization and all its associated projects and environments."
    );

    // --------------------------------------------------------------------------------------------------------------------
    // Demonstrate other authenticated operations here
    // --------------------------------------------------------------------------------------------------------------------
    // For example, you can now perform operations that require authentication, such as accessing user data,
    // loading environments, or managing projects and organizations.

    // --------------------------------------------------------------------------------------------------------------------
    // Logging out of SwitchKeys
    // --------------------------------------------------------------------------------------------------------------------
    // Finally, log out of SwitchKeys.
    switchkeys.auth.logout();
    console.log("[+] Logged out successfully.");
  }
}
