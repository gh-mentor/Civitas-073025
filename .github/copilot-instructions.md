# Copilot Instructions for JavaScript Code Generation

## General Guidelines
- Use camelCase for variable and function names.
- Use PascalCase for class names.
- Use single quotes for strings.
- Ensure all functions have JSDoc comments.
- Ensure consistent indentation using 2 spaces.
- Alwaysimplement the TODOs in the generated code.

## Specific Instructions
- Use `const` for variables that do not change.
- Use `let` instead of `var` for variable declarations.
- Prefer arrow functions for anonymous functions.
- Use template literals instead of string concatenation.
- Ensure all async functions handle errors using try-catch.
- Verify that all imported modules are used.
- Check for proper error handling in all functions.
- Ensure all loops have proper termination conditions.
- Use descriptive names for variables and functions.
- Avoid deeply nested code; refactor into smaller functions if necessary.
- Ensure all promises are properly awaited.
- Verify that all dependencies are listed in `package.json`.
- Check for any potential performance issues.

## Example Code Snippet
```javascript
// Good example of a function with proper naming and error handling
/**
 * Fetches user data from the API.
 * @param {string} userId - The ID of the user.
 * @returns {Promise<Object>} The user data.
 */
const fetchUserData = async (userId) => {
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    throw error;
  }
};