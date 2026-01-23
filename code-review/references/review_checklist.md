# Code Review Checklist

This document provides a comprehensive checklist for systematic code review. Use this as a reference when performing code review to ensure thorough analysis.

## Logic Error Checklist

### Control Flow
- [ ] All conditional branches are reachable
- [ ] Switch/case statements have default cases where appropriate
- [ ] Loop termination conditions are correct
- [ ] No infinite loops or unreachable code
- [ ] Early returns are used appropriately
- [ ] Exception handling covers all error paths

### Data Access
- [ ] Array/collection bounds are checked before access
- [ ] No off-by-one errors in loops
- [ ] Null/None checks are performed before dereferencing
- [ ] Type conversions are explicit and safe
- [ ] Division by zero is prevented
- [ ] Overflow/underflow is handled for numeric operations

### State Management
- [ ] State transitions are valid and complete
- [ ] Initialization happens before use
- [ ] State is consistent after operations
- [ ] Race conditions are prevented in concurrent code
- [ ] Shared state is properly synchronized

### Algorithm Correctness
- [ ] Algorithm logic matches intended behavior
- [ ] Edge cases are handled (empty inputs, single elements, etc.)
- [ ] Boundary conditions are tested
- [ ] Mathematical operations are correct

## Format Error Checklist

### Code Style
- [ ] Consistent indentation (spaces or tabs, not mixed)
- [ ] Line length adheres to project standards
- [ ] Consistent spacing around operators
- [ ] Consistent brace/block style
- [ ] No trailing whitespace
- [ ] Consistent newline style (LF vs CRLF)

### Naming Conventions
- [ ] Functions follow naming convention (camelCase, snake_case, PascalCase)
- [ ] Variables follow naming convention
- [ ] Constants are clearly identified
- [ ] Names are descriptive and meaningful
- [ ] No abbreviations unless widely understood

### Documentation
- [ ] Public functions have docstrings/comments
- [ ] Complex logic has explanatory comments
- [ ] TODO/FIXME comments are justified
- [ ] Comments are up-to-date with code
- [ ] No commented-out code blocks

### Organization
- [ ] Imports are organized and grouped
- [ ] Unused imports are removed
- [ ] Code is logically grouped
- [ ] Related functions are placed together
- [ ] File structure follows project conventions

## Redundancy Analysis Checklist

### Unused Code
- [ ] All defined functions are called somewhere
- [ ] All declared variables are used
- [ ] All imports are used
- [ ] No dead code paths
- [ ] No unreachable code after certain conditions
- [ ] No commented-out code that should be removed

### Code Duplication
- [ ] No identical code blocks
- [ ] Similar patterns are abstracted
- [ ] No copy-paste code
- [ ] Repeated logic is extracted to functions
- [ ] Magic numbers/strings are extracted to constants

### Extractable Helpers
- [ ] Long functions are broken into smaller pieces
- [ ] Complex expressions are simplified with helpers
- [ ] Single-responsibility functions are identified
- [ ] Utility functions are reusable
- [ ] Common patterns are abstracted

## Memory Leak Checklist

### File Handles
- [ ] All file handles are closed
- [ ] Context managers (`with` statements) are used where appropriate
- [ ] Files are closed in exception paths
- [ ] No file handles left open in loops

### Dynamic Memory
- [ ] All allocated memory is freed
- [ ] No memory allocated but never used
- [ ] Proper cleanup in destructors
- [ ] No circular references preventing GC
- [ ] Large objects are explicitly deleted when no longer needed

### Collections
- [ ] Collections don't grow unbounded
- [ ] Old entries are removed when no longer needed
- [ ] Cache eviction policies are implemented
- [ ] No memory-intensive operations in tight loops

### Resources
- [ ] Database connections are closed
- [ ] Network sockets are closed
- [ ] Streams are properly closed
- [ ] Locks are released
- [ ] Context managers are used for resource management

## Thread Leak Checklist

### Thread Lifecycle
- [ ] All started threads have exit conditions
- [ ] Threads are properly joined or detached
- [ ] Thread pools are properly shut down
- [ ] No threads that run indefinitely
- [ ] Thread cleanup happens in error paths

### Synchronization
- [ ] Locks are acquired and released in pairs
- [ ] No deadlock potential
- [ ] Proper use of condition variables
- [ ] Thread-safe data structures are used where needed
- [ ] Race conditions are prevented

### Thread-Local Storage
- [ ] Thread-local storage is cleaned up
- [ ] No accumulation of thread-local data
- [ ] Proper thread pool management

## Optimization Checklist

### Algorithm Efficiency
- [ ] Algorithms use appropriate time complexity
- [ ] Data structures are chosen appropriately
- [ ] No unnecessary nested loops
- [ ] Early exits are used where possible
- [ ] Lazy evaluation is used where beneficial

### Computation
- [ ] No redundant calculations in loops
- [ ] Results are cached where appropriate
- [ ] Expensive operations are minimized
- [ ] String concatenation uses efficient methods
- [ ] No unnecessary object creation

### I/O Operations
- [ ] Database queries are optimized
- [ ] Batch operations are used where possible
- [ ] Network calls are minimized
- [ ] File I/O is buffered appropriately
- [ ] No redundant API calls

### Code Quality
- [ ] Design patterns are used appropriately
- [ ] Code is maintainable and readable
- [ ] Separation of concerns is clear
- [ ] Dependencies are minimized
- [ ] Code is testable

## Language-Specific Checklists

### Python
- [ ] Context managers used for resources
- [ ] Generators used for large sequences
- [ ] Proper exception handling
- [ ] Thread safety considered (GIL)
- [ ] Async/await used appropriately
- [ ] Type hints where beneficial

### TypeScript/JavaScript
- [ ] Promises are properly handled
- [ ] Event listeners are removed
- [ ] Timers/intervals are cleared
- [ ] Closures don't leak memory
- [ ] WeakMap/WeakSet used where appropriate
- [ ] Proper async/await error handling

### C/C++
- [ ] RAII patterns used
- [ ] Smart pointers used appropriately
- [ ] No raw pointer leaks
- [ ] Buffer overflows prevented
- [ ] Mutexes properly locked/unlocked
- [ ] Exception safety guaranteed

## Review Process

1. **Initial Scan**: Read through code to understand structure and purpose
2. **Logic Review**: Check for logical errors and correctness
3. **Format Check**: Verify code style and formatting
4. **Redundancy Analysis**: Identify unused code and duplication
5. **Resource Analysis**: Check for leaks and resource management
6. **Optimization Review**: Identify performance improvements
7. **Final Summary**: Compile findings with priorities

## Severity Levels

- **Critical**: Bugs that cause crashes, data corruption, or security issues
- **High**: Issues that cause incorrect behavior or significant performance problems
- **Medium**: Code quality issues that affect maintainability or moderate performance
- **Low**: Minor style issues or optimization opportunities with minimal impact
