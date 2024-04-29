// Import the SwitchKeys class from the client library.
// import SwitchKeys from "switchkeys";
import SwitchKeys from "../switchkeys/core/base";

export async function environmenthExample() {
  const switchkeys = new SwitchKeys();

  const environmentKey = "16e78bfa-fa85-4313-8bc2-1bd09db34642";

  // Load the whole environment
  // const environment = await switchkeys.environments.load(environmentKey)
  // console.log(environment)

  // Load the environment project
  // const project = await switchkeys.environments.getProject(environmentKey)
  // console.log(project)

  // Load the environment organization
  // const organization = await switchkeys.environments.getOrganization(environmentKey)
  // console.log(organization)

  // Load the environment users
  // const users = await switchkeys.environments.getUsers(environmentKey)
  // console.log(users[1].features)

  // Load the environment users
  // const users = await switchkeys.environments.getUsers(environmentKey)
  // console.log(users[1].features)

  // Load the environment features
  // const features = await switchkeys.environments.getFeatures(environmentKey)
  // console.log(features[0].name)

  // Get user details, e.g. the user features or user device.
  // const user = await switchkeys.environments.users.get(environmentKey, {
  //   username: 'Adham'
  // })

  // console.log(user.device.version)

  const user = await switchkeys.environments.users.get(environmentKey, {
    username: "Maged",
  });

  if (user.hasFeature("debug")){
    user.getFeature('debug')
  }

  user.setFeature({name: 'theme', value: 'green'})
  console.log(user.features)
}
