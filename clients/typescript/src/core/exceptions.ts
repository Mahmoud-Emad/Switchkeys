import { SwitchKeysLogger } from "../utils/logger";

const logger: SwitchKeysLogger = new SwitchKeysLogger();

/**
 * Custom error class for representing connection errors in SwitchKeys.
 */
class SwitchKeysConnectionError extends Error {
  /**
   * Constructs a new SwitchKeysConnectionError with the specified error message.
   * @param message The error message.
   */
  constructor(message: string) {
    super(message);
    logger.error(message);
  }
}

/**
 * Custom error class for representing database record not found errors in SwitchKeys.
 */
class SwitchKeysRecordNotFoundError extends Error {
  /**
   * Constructs a new `SwitchKeysRecordNotFoundError` with the specified error message.
   * @param message The error message.
   */
  constructor(message: string) {
    super(message);
    logger.error(message);
  }
}

/**
 * Custom error class for representing unauthorized errors in SwitchKeys.
 */
class SwitchKeysUnauthorizedError extends Error {
  /**
   * Constructs a new SwitchKeysUnauthorizedError with the specified error message.
   * @param message The error message.
   */
  constructor(message: string) {
    super(message);
    logger.error(message);
  }
}

/**
 * Custom error class for representing validation errors in SwitchKeys.
 */
class SwitchKeysValidationError extends Error {
  /**
   * Constructs a new SwitchKeysValidationError with the specified error message.
   * @param message The error message.
   */
  constructor(message: string) {
    super(message);
    logger.error(message);
  }
}

/**
 * Custom error class for representing feature not exist errors in SwitchKeys.
 */
class SwitchKeysFeatureDoesNotExistError extends Error {
  /**
   * Constructs a new `SwitchKeysFeatureDoesNotExistError` with the specified error message.
   * @param message The error message.
   */
  constructor(message: string) {
    super(message);
    logger.error(message);
  }
}

export {
  SwitchKeysConnectionError,
  SwitchKeysRecordNotFoundError,
  SwitchKeysUnauthorizedError,
  SwitchKeysValidationError,
  SwitchKeysFeatureDoesNotExistError,
};
