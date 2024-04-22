import * as dotenv from "dotenv";

dotenv.config(); // Load environment variables from .env file

/**
 * Represents authentication routes for making API requests.
 */
class SwitchKeysAuthRoutes {
  private BASE_URL: string;

  /**
   * Constructs a new SwitchKeysAuthRoutes instance.
   */
  constructor() {
    this.BASE_URL = process.env.BASE_URL || "";
  }

  /**
   * Gets the URL for user registration.
   * @returns The URL for user registration.
   */
  get registerURL(): string {
    return `${this.BASE_URL}/api/auth/signup/`;
  }

  /**
   * Gets the URL for user login.
   * @returns The URL for user login.
   */
  get loginURL(): string {
    return `${this.BASE_URL}/api/auth/login/`;
  }
}

/**
 * Represents user routes for making API requests.
 */
class SwitchKeysUserRoutes {
  private BASE_URL: string;

  /**
   * Constructs a new `SwitchKeysUserRoutes` instance.
   */
  constructor() {
    this.BASE_URL = process.env.BASE_URL || "";
  }

  /**
   * Gets the URL for user by its ID.
   * @returns The URL for getting a user.
   */
  getById(id: number): string {
    return `${this.BASE_URL}/api/users/${id}/`;
  }

  /**
   * Gets the URL for user by its ID.
   * @returns The URL for getting a user.
   */
  getByEmail(userEmail: string): string {
    return `${this.BASE_URL}/api/users/email/${userEmail}/`;
  }
}

/**
 * Represents organization routes for making API requests.
 */
class SwitchKeysOrganizationRoutes {
  private BASE_URL: string;

  /**
   * Constructs a new `SwitchKeysUserRoutes` instance.
   */
  constructor() {
    this.BASE_URL = process.env.BASE_URL || "";
  }

  /**
   * Gets the URL for organization by its ID.
   * @returns The URL for getting an organization.
   */
  get create(): string {
    return `${this.BASE_URL}/api/organizations/`;
  }

  /**
   * Gets the URL for organization by its ID.
   * @returns The URL for getting an organization.
   */
  getById(id: number): string {
    return `${this.BASE_URL}/api/organizations/${id}/`;
  }

  /**
   * Gets the URL for adding a member on organization by its ID.
   * @returns The URL for getting an organization adding member.
   */
  addMember(id: number): string {
    return `${this.BASE_URL}/api/organizations/${id}/add-member/`;
  }

  /**
   * Gets the URL for removing a member on organization by its ID.
   * @returns The URL for getting an organization removing member.
   */
  removeMember(id: number): string {
    return `${this.BASE_URL}/api/organizations/${id}/remove-member/`;
  }
}

/**
 * Represents API routes for making requests.
 */
class SwitchKeysApiRoutes {
  static auth: SwitchKeysAuthRoutes = new SwitchKeysAuthRoutes();
  static members: SwitchKeysUserRoutes = new SwitchKeysUserRoutes();
  static organizations: SwitchKeysOrganizationRoutes =
    new SwitchKeysOrganizationRoutes();
}

export { SwitchKeysApiRoutes };
