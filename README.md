# Secure Concurrent Banking System with AI Adaptability 

## Project Overview
This repository contains the Capstone project for the Advanced Object-Oriented Design and Programming module. It is a highly secure, multithreaded banking engine designed with strict state management (RLock) to prevent deadlocks and race conditions. Furthermore, the architecture is extended using advanced GoF Design Patterns to integrate scalable AI fraud-detection components.

## Advanced Design Patterns Implemented
1. **Decorator Pattern:** Used for non-intrusive Security Auditing and Logging for SOC/GRC compliance.
2. **Strategy Pattern:** Enables runtime flexibility to switch between different AI risk-evaluation algorithms.
3. **Abstract Factory Pattern:** Provides an interface to securely instantiate Cloud-based or On-premise Edge AI models without vendor lock-in.

## Folder Structure
- `/src`: Contains the core banking logic and OO pattern implementations.
- `/tests`: Contains comprehensive unit tests, including AI component isolation using the `unittest.mock` framework.
- `/docs`: Contains UML Class and Sequence diagrams visualising the architecture.

## How to Run the Application
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
