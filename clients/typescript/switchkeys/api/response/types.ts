import { SwitchKeysAuthTokens } from "../../utils/types";

interface ISwitchKeysAuthRegisterResponse{
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  joiningAt: string;
  accessToken: string;
  refreshToken: string;
}

class SwitchKeysTokensResponse implements SwitchKeysAuthTokens {
  accessToken: string | undefined;
  refreshToken: string | undefined;

  constructor(accessToken?: string, refreshToken?: string) {
    this.accessToken = accessToken;
    this.refreshToken = refreshToken;
  }
}

class SwitchKeysAuthRegisterResponse implements ISwitchKeysAuthRegisterResponse{
  id: number = 0;
  firstName: string = "";
  lastName: string = "";
  email: string = "";
  joiningAt: string = "";
  userType: string = "";
  accessToken: string = "";
  refreshToken: string = "";

  parseAuth(authData: any){
    this.id = authData['id']
    this.firstName = authData['first_name']
    this.lastName = authData['last_name']
    this.joiningAt = authData['joining_at']
    this.userType = authData['user_type']
    this.accessToken = authData['access_token']
    this.refreshToken = authData['refresh_token']
  }
}

export { SwitchKeysTokensResponse, SwitchKeysAuthRegisterResponse };
