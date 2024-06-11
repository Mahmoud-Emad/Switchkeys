/**
 * Validates the provided password against the following strong password rules:
 *
 * - At least one uppercase letter
 * - At least one lowercase letter
 * - At least one digit
 * - At least one special character
 * - Minimum length of 8 characters
 *
 * @param {string} password - The password to be validated.
 * @returns {boolean | string} - Returns true if the password meets all the rules, otherwise returns a message indicating which rule(s) the password does not meet.
 */
export function isStrongPasswordRules(password: string): boolean | string {
  const minLength = 8
  const hasUpperCase = /[A-Z]/.test(password)
  const hasLowerCase = /[a-z]/.test(password)
  const hasDigit = /[0-9]/.test(password)
  const hasSpecialChar = /[!@#$%^&+*(),.?":{}|<>]/.test(password)
  const hasMinLength = password && password.length >= minLength

  if (!password) {
    return 'The password is required.'
  }
  if (!hasUpperCase) {
    return 'The password should have at least one uppercase letter.'
  }
  if (!hasLowerCase) {
    return 'The password should have at least one lowercase letter.'
  }
  if (!hasDigit) {
    return 'The password should have at least one digit.'
  }
  if (!hasSpecialChar) {
    return 'The password should have at least one special character.'
  }
  if (!hasMinLength) {
    return 'The password should have a minimum length of 8 characters.'
  }
  return true
}

/**
 * Validates the provided email against a standard email format.
 *
 * @param {string} email - The email address to be validated.
 * @returns {boolean | string} - Returns true if the email is valid, otherwise returns a message indicating the email is invalid.
 */
export function isValidEmailRules(email: string): boolean | string {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

  if (!email) {
    return 'The email address is required.'
  }
  if (!emailRegex.test(email)) {
    return 'The email address is invalid.'
  }
  return true
}

/**
 * Validates the provided name (first name or last name) based on the specified rules:
 * - Minimum length of 3 characters
 * - Maximum length of 10 characters
 *
 * @param {string} name - The name to be validated.
 * @returns {boolean | string} - Returns true if the name is valid, otherwise returns a message indicating the validation error.
 */
export function isValidNameRules(name: string): boolean | string {
  const minLength = 3
  const maxLength = 10
  const specialCharRegex = /[!@#$%^&*(),.?":{}|<>0-9]/

  if (!name) {
    return `This field is required.`
  }
  if (name.length < minLength) {
    return `The name should be at least ${minLength} characters long.`
  }
  if (name.length > maxLength) {
    return `The name should not exceed ${maxLength} characters.`
  }
  if (specialCharRegex.test(name)) {
    return `The name should not contain special characters or numbers.`
  }
  return true
}
