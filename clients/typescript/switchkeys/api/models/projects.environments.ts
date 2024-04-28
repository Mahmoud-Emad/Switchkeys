import SwitchKeysEnvironmentUser from "./environment.users";
import SwitchKeysEnvironmentFeatures from "./envoronment.features";

class SwitchKeysEnvironment{
  features: SwitchKeysEnvironmentFeatures = new SwitchKeysEnvironmentFeatures()
  users: SwitchKeysEnvironmentUser = new SwitchKeysEnvironmentUser()

  async load(){}
  async getProject(){}
  async getOrganization(){}
}

export default SwitchKeysEnvironment;