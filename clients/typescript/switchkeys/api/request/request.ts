import * as dotenv from 'dotenv';

dotenv.config(); // Load environment variables from .env file

class SwitchKeysAuthRoutes {
  private BASE_URL = process.env.BASE_URL;
  registerURL = `${this.BASE_URL}/api/auth/signup/`;
  loginURL = `${this.BASE_URL}/api/auth/login/`;
}

class SwitchKeysApiRoutes {
  static auth: SwitchKeysAuthRoutes = new SwitchKeysAuthRoutes();
}

export { SwitchKeysApiRoutes };
