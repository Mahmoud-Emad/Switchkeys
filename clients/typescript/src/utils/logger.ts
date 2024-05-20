/**
 * Utility class for logging messages with timestamps and colored output.
 */
class SwitchKeysLogger {
  private now: Date;
  private time: string;

  /**
   * Creates an instance of SwitchKeysLogger.
   */
  constructor() {
    this.now = new Date();
    this.time = `└─(${this.now.getHours()}:${this.now.getMinutes()}:${this.now.getSeconds()})──> `;
  }

  /**
   * Logs an error message in red color with a timestamp.
   * @param message - The error message to log.
   */
  error(message: string): void {
    console.error(`${this.time} \x1b[31m${message}\x1b[0m`); // Red color
  }

  /**
   * Logs a log message in gray color with a timestamp.
   * @param message - The log message to log.
   */
  log(message: string): void {
    console.log(`${this.time} \x1b[90m${message}\x1b[0m`); // Gray color
  }

  /**
   * Logs a warning message in yellow color with a timestamp.
   * @param message - The warning message to log.
   */
  warning(message: string): void {
    console.warn(`${this.time} \x1b[33m${message}\x1b[0m`); // Yellow color
  }

  /**
   * Logs an info message in blue color with a timestamp.
   * @param message - The info message to log.
   */
  info(message: string): void {
    console.log(`${this.time} \x1b[34m${message}\x1b[0m`); // Blue color
  }
}

export { SwitchKeysLogger };
