/**
 * Generates a strong password.
 * The password includes at least one uppercase letter, one lowercase letter, one number, and one special character.
 * The remaining characters are filled randomly from the entire character set and then shuffled to avoid predictable patterns.
 *
 * @param {number} [length=12] - The length of the generated password. Default is 12.
 * @returns {string} - The generated strong password.
 */
export function generateStrongPassword(length = 12): string {
  const upperCaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  const lowerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'
  const numbers = '0123456789'
  const specialCharacters = '!@#$%^&+*(),.?":{}|<>'

  const allCharacters =
    upperCaseLetters + lowerCaseLetters + numbers + specialCharacters

  let password = ''

  // Ensure the password has at least one character from each category
  password +=
    upperCaseLetters[Math.floor(Math.random() * upperCaseLetters.length)]
  password +=
    lowerCaseLetters[Math.floor(Math.random() * lowerCaseLetters.length)]
  password += numbers[Math.floor(Math.random() * numbers.length)]
  password +=
    specialCharacters[Math.floor(Math.random() * specialCharacters.length)]

  // Generate the remaining characters randomly from all categories
  for (let i = password.length; i < length; i++) {
    password += allCharacters[Math.floor(Math.random() * allCharacters.length)]
  }

  // Shuffle the password to avoid predictable patterns
  password = password
    .split('')
    .sort(() => 0.5 - Math.random())
    .join('')

  return password
}

/**
 * The generateCardLogo function generates a logo by extracting the first two uppercase characters from a given name. If there are fewer than two uppercase characters, it defaults to the first two characters of the name.
 *
 * @param {string} name - The name to generate a logo from it.
 * @returns {string} - The generated logo.
 */
export function generateCardLogo(name: string) {
  const chars = name
    .replace(' ', '')
    .split('')
    .filter((char) => char === char.toUpperCase())
  return chars.length >= 2 ? `${chars[0]}${chars[1]}` : `${name[0]}${name[1]}`
}
