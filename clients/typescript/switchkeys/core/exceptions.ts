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
   * Constructs a new SwitchKeysConnectionError with the specified error message.
   * @param message The error message.
   */
  constructor(message: string) {
    super(message);
    logger.error(message);
  }
}

export { SwitchKeysConnectionError, SwitchKeysRecordNotFoundError };
