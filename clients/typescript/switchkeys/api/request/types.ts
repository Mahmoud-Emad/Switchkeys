import { SwitchKeysUserType } from "../../utils/types";

interface SwitchKeysAuthRegisterData {
  email: string;
  password: string;
  firstName: string;
  lastName: string;
  userType?: SwitchKeysUserType;
}

interface SwitchKeysAuthLoginData {
  email: string;
  password: string;
}

export {
  SwitchKeysAuthRegisterData,
  SwitchKeysAuthLoginData,
};
