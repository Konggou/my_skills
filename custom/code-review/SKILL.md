---
name: code-review
description: This skill should be used when users request code review, code analysis, or code quality assessment. It provides systematic code review workflows that check for logic errors, format issues, redundant code, memory/thread leaks, and optimization opportunities. The skill only provides review feedback and suggestions, never modifies code directly.
---

# Code Review

## Overview

This skill enables systematic code review following a structured workflow. It analyzes code for logic errors, format issues, code redundancy, resource leaks, and optimization opportunities. The skill provides comprehensive review feedback and suggestions without modifying the code.

## When to Use This Skill

Use this skill when:
- Users request code review, code analysis, or code quality checks
- Users ask to check for bugs, errors, or issues in code
- Users want optimization suggestions or refactoring recommendations
- Users need to identify unused code, redundant functions, or extractable helpers
- Users want to assess memory safety, thread safety, or resource management

## Code Review Workflow

Follow this sequential workflow when performing code review:

### Step 1: Logic and Format Error Check

Examine the code for logical errors and format issues:

**Logic Errors:**
- Check for off-by-one errors in loops and array access
- Verify conditional logic correctness (if/else, switch statements)
- Validate error handling paths and exception handling
- Check for null pointer dereferences and undefined behavior
- Verify type consistency and implicit conversions
- Check for race conditions in concurrent code
- Validate state transitions and state machine logic
- Check for infinite loops or unreachable code

**Format Errors:**
- Check indentation consistency (spaces vs tabs)
- Verify line length and code style adherence
- Check for missing or extra whitespace
- Validate naming conventions (functions, variables, classes)
- Check for missing docstrings or comments where needed
- Verify import organization and unused imports
- Check for trailing whitespace or inconsistent newlines

**Output Format:**
- List each logic error with: file path, line number, error description, and potential impact
- List each format error with: file path, line number, and suggested fix
- Prioritize errors by severity (critical, warning, minor)

### Step 2: Redundancy Analysis

Identify redundant code, unused functions/variables, and extractable helper functions:

**Unused Code Detection:**
- Find functions that are defined but never called
- Identify variables that are declared but never used
- Check for unused imports or dependencies
- Look for dead code paths (unreachable after certain conditions)
- Identify duplicate code blocks that could be consolidated

**Extractable Helper Functions:**
- Identify repeated code patterns that could be extracted into functions
- Find complex expressions that could be simplified with helper functions
- Look for code blocks that perform single, well-defined operations
- Check for long functions that could be broken down into smaller helpers
- Identify utility functions that could be reused across modules

**Code Duplication:**
- Find identical or near-identical code blocks
- Identify similar patterns that could use shared abstractions
- Check for copy-paste code that should be refactored

**Output Format:**
- List unused functions/variables with: file path, line number, and removal suggestion
- List extractable helpers with: code location, suggested function signature, and rationale
- List duplicate code with: locations of duplicates and suggested consolidation approach

### Step 3: Memory and Thread Leak Analysis

Analyze code for resource management issues:

**Memory Leak Detection:**
- Check for unclosed file handles (missing `close()` or context managers)
- Verify proper cleanup of dynamically allocated resources
- Check for circular references that prevent garbage collection
- Identify objects that accumulate in collections without cleanup
- Check for missing `del` statements for large objects
- Verify proper use of context managers (`with` statements)
- Check for unclosed database connections or network sockets
- Identify memory-intensive operations that could be optimized

**Thread Leak Detection:**
- Check for threads that are started but never joined
- Verify proper thread pool shutdown and cleanup
- Check for threads that run indefinitely without exit conditions
- Identify race conditions in thread synchronization
- Verify proper use of locks and deadlock prevention
- Check for thread-local storage that isn't cleaned up
- Identify threads that block indefinitely

**Resource Management:**
- Check for proper exception handling that ensures resource cleanup
- Verify use of try-finally or context managers for cleanup
- Check for resources acquired but not released in error paths
- Identify missing cleanup in destructors or finalizers

**Output Format:**
- List memory leaks with: file path, line number, resource type, and cleanup suggestion
- List thread leaks with: file path, line number, thread description, and lifecycle management suggestion
- Provide severity assessment (critical, high, medium, low)

### Step 4: Optimization Suggestions

Analyze code performance and provide optimization recommendations:

**Performance Analysis:**
- Identify inefficient algorithms (O(n²) that could be O(n log n))
- Find unnecessary computations in loops
- Check for redundant database queries or API calls
- Identify opportunities for caching or memoization
- Check for inefficient data structures (list vs set, dict vs list)
- Find string concatenation in loops (should use join)
- Identify opportunities for lazy evaluation
- Check for premature optimization or over-optimization

**Code Quality Improvements:**
- Suggest better design patterns where applicable
- Recommend improved error handling strategies
- Suggest better separation of concerns
- Identify opportunities for dependency injection
- Recommend better abstraction layers
- Suggest improved testability improvements

**Best Practices:**
- Recommend adherence to language-specific best practices
- Suggest improvements for maintainability
- Recommend better documentation or type hints
- Suggest improvements for code readability

**Output Format:**
- List optimizations with: file path, line number, current approach, suggested improvement, and expected benefit
- Prioritize by impact (high, medium, low)
- Provide code examples for suggested improvements where helpful

## Review Output Structure

When providing code review feedback, structure the output as follows:

```markdown
# Code Review Report

## Summary
[Brief overview of findings: total issues found, severity breakdown]

## 1. Logic and Format Errors
### Critical Issues
- [Issue description with location]

### Warnings
- [Issue description with location]

### Format Issues
- [Issue description with location]

## 2. Redundancy Analysis
### Unused Code
- [Unused function/variable with location]

### Extractable Helpers
- [Code pattern that could be extracted]

### Code Duplication
- [Duplicate code locations]

## 3. Memory and Thread Leak Analysis
### Memory Leaks
- [Resource leak with location and fix]

### Thread Leaks
- [Thread issue with location and fix]

### Resource Management
- [Resource management issue]

## 4. Optimization Suggestions
### High Impact
- [Optimization with expected benefit]

### Medium Impact
- [Optimization suggestion]

### Low Impact / Code Quality
- [Quality improvement suggestion]
```

## Important Guidelines

1. **Never modify code directly** - Only provide review feedback and suggestions
2. **Be specific** - Always include file paths and line numbers when possible
3. **Prioritize** - Focus on critical issues first (logic errors, memory leaks)
4. **Provide context** - Explain why something is an issue, not just that it is
5. **Be constructive** - Frame suggestions as improvements, not just problems
6. **Consider trade-offs** - Acknowledge when optimizations might have downsides
7. **Language-aware** - Adapt checks to the specific programming language being reviewed
8. **Project-aware** - Consider the project's coding standards and architecture when making suggestions

## Language-Specific Considerations

### Python
- Check for proper use of context managers
- Verify exception handling and cleanup
- Check for proper use of generators vs lists
- Verify thread safety with GIL considerations
- Check for proper use of async/await patterns

### TypeScript/JavaScript
- Check for proper promise handling and cleanup
- Verify event listener removal
- Check for memory leaks in closures
- Verify proper cleanup of timers/intervals
- Check for proper use of WeakMap/WeakSet

### C/C++
- Check for proper memory allocation/deallocation
- Verify RAII patterns
- Check for buffer overflows
- Verify proper use of smart pointers
- Check for proper mutex/condition variable usage

## Resources

### references/
See `references/review_checklist.md` for a detailed checklist of items to verify during code review.

### scripts/
No scripts are included as code review is primarily an analytical task. However, static analysis tools can complement manual review.
