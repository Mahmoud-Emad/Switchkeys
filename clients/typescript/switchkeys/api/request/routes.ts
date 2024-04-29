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
 * Represents project routes for making API requests.
 */
class SwitchKeysProjectRoutes {
  private BASE_URL: string;

  /**
   * Constructs a new SwitchKeysAuthRoutes instance.
   */
  constructor() {
    this.BASE_URL = process.env.BASE_URL || "";
  }

  /**
   * Gets the URL for creating a project.
   * @returns The URL for creating a project.
   */
  get create(): string {
    return `${this.BASE_URL}/api/projects/`;
  }

  /**
   * Gets the URL for project by its ID.
   * @returns The URL for getting an project.
   */
  getById(id: number): string {
    return `${this.BASE_URL}/api/projects/${id}/`;
  }

  /**
   * Gets the URL for all organization projects.
   * @returns The URL for all organization projects.
   */
  getAllOrganizationProjects(id: number): string {
    return `${this.BASE_URL}/api/organizations/${id}/projects/`;
  }
}

/**
 * Represents environment routes for making API requests.
 */
class SwitchKeysEnvironmentRoutes {
  private BASE_URL: string;

  /**
   * Constructs a new `SwitchKeysEnvironmentRoutes` instance.
   */
  constructor() {
    this.BASE_URL = process.env.BASE_URL || "";
  }

  /**
   * Gets the URL for creating a environment.
   * @returns The URL for creating a environment.
   */
  get create(): string {
    return `${this.BASE_URL}/api/environments/`;
  }

  /**
   * Gets the URL for environment by its ID.
   * @returns The URL for getting an environment.
   */
  load(environmentKey: string): string {
    return `${this.BASE_URL}/api/environments/key/${environmentKey}/`;
  }

  /**
   * Gets the URL for adding a feature for a user on environment by the environment key.
   * @returns The URL for adding a feature for a user on environment by the environment key.
   */
  addFeature(environmentKey: string): string {
    return `${this.BASE_URL}/api/environments/key/${environmentKey}/user/add-feature/`;
  }
}

/**
 * Represents API routes for making requests.
 */
class SwitchKeysApiRoutes {
  static auth: SwitchKeysAuthRoutes = new SwitchKeysAuthRoutes();
  static members: SwitchKeysUserRoutes = new SwitchKeysUserRoutes();
  static projects: SwitchKeysProjectRoutes = new SwitchKeysProjectRoutes();
  static environments: SwitchKeysEnvironmentRoutes = new SwitchKeysEnvironmentRoutes();
  static organizations: SwitchKeysOrganizationRoutes =
    new SwitchKeysOrganizationRoutes();
}

export { SwitchKeysApiRoutes };
