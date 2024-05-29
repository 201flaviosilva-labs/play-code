# BestMathScore

## Purpose

The `BestMathScore` class helps to find the best mathematical equation using a set of numbers and operators. It tries different combinations of these numbers and operators to see which one produces the highest result (score).

## How It Works

1. **Initialization:** The class starts with a set of numbers, operators, and some settings.
2. **Running:** It creates multiple random equations, solves them, and keeps track of the highest result (best score).
3. **Output:** After a set number of attempts (iterations), it tells you the best equation it found and what that equation's result is.

## Key Features

- **Numbers and Operators:** You can choose which numbers (e.g., `[1, 2, 3]`) and operators (e.g., `['+', '-']`) to use.
- **Iterations:** You can decide how many times (up to `maxIterations`) it should try different equations.
- **Repeat Numbers:** You can allow or disallow the reuse of the same number in an equation.
- **Equation Length:** You can control how long the equations can be using `maxEquationLength`.

## Example Usage

### Step 1: Define Settings

Set up the class with your chosen numbers, operators, and other settings.

```js
const best = new BestMathScore({
	maxIterations: 1000,
	repeatNumbers: true,
});
```

- `maxIterations: 1000` – It will try up to 1000 different equations.
- `repeatNumbers: true` – It can use the same number more than once in an equation.

### Step 2: Run the Calculation

Call the `run()` method to start the process.

```js
best.run();
```

### Step 3: See the Results

The class will print out data after each iteration. After finishing, it will tell you the best equation and its score.

## Explanation of Main Methods

- **Constructor:** Sets up the class with your chosen settings.
- **run():** This is the main method. It repeatedly creates and evaluates new equations.
- **step():** Generates one random equation and evaluates it.
- **_randomizeEquation():** Creates a new random equation using the given numbers and operators.
- **_equationToString(equation):** Converts the equation array into a string for easy reading.

### Example Output

After running the class, you might get outputs like this during each iteration:

```plaintext
{
	iteration: 1,
	score: 5,
	current: "1+4",
	bestScore: 5,
	bestIteration: "1+4"
}
...
Best score: 10 in 1000 iterations, equation: "5+5"
```

- **`iteration`:** Shows the current attempt number.
- **`score`:** The result of the current equation.
- **`current`:** The equation tried in this iteration.
- **`bestScore`:** The highest result found so far.
- **`bestIteration`:** The equation that gave the best result so far.

This class essentially helps to automate the search for the highest-scoring equation based on your criteria, making it a useful tool for exploring mathematical combinations.
