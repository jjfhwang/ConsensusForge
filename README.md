# ConsensusForge: A Byzantine-Fault Tolerant State Machine Experiment

ConsensusForge is a Python-based project designed for experimenting with decentralized state machines. It implements a Byzantine Fault Tolerance (BFT) consensus mechanism based on Proof-of-Stake (PoS) and provides a smart contract execution environment for WebAssembly (WASM) bytecode, offering a platform for researchers and developers to explore the possibilities of distributed, secure, and programmable applications.

This repository provides a playground to prototype and evaluate various BFT consensus algorithms in a simulated environment. It leverages Python's rapid prototyping capabilities for ease of experimentation and extensibility. Unlike traditional centralized systems, ConsensusForge aims to demonstrate resilience against malicious actors by ensuring that even if a certain number of validators act dishonestly, the system as a whole can still reach a consistent and valid state. The integration of WASM smart contracts allows for the development of complex applications that can be deployed and executed in a decentralized manner, expanding the possibilities for blockchain-based solutions beyond simple value transfer. This project is intended for research, educational purposes, and as a foundational component for more complex decentralized systems.

ConsensusForge is more than just a theoretical exercise. It offers a practical implementation of a distributed ledger technology, allowing users to observe the behavior of the consensus algorithm under various network conditions and attack scenarios. By providing a WASM execution environment, the project enables developers to deploy and test smart contracts in a controlled setting, experimenting with different contract architectures and exploring the limits of decentralized computation. The modular design of ConsensusForge allows for easy modification and extension, making it a valuable tool for exploring different aspects of decentralized state machine replication. The project aims to contribute to a better understanding of the challenges and opportunities associated with building robust and scalable decentralized systems.

The primary goal of ConsensusForge is to provide a flexible and extensible platform for experimentation. It is not intended to be a production-ready blockchain implementation, but rather a tool for research, education, and prototyping. The project focuses on providing a clear and concise implementation of the core concepts behind BFT consensus and smart contract execution, allowing users to easily understand and modify the code. The WASM execution environment is designed to be secure and efficient, but it is not optimized for performance. The project is constantly evolving, with new features and improvements being added regularly. Contributions from the community are welcome and encouraged.

## Key Features

*   **BFT Consensus via Proof-of-Stake:** Implements a Proof-of-Stake based BFT consensus algorithm, designed to tolerate a certain percentage of Byzantine (malicious) nodes. The algorithm uses a voting mechanism where validators stake tokens to participate in the consensus process. Each validator proposes and votes on blocks, and the block with the most stake-weighted votes is considered valid.

*   **WASM Smart Contract Execution Environment:** Provides a secure and sandboxed environment for executing WASM bytecode. Smart contracts are deployed to the network and executed by validators, enabling decentralized application logic. The WASM engine is designed to be efficient and secure, preventing malicious contracts from disrupting the network.

*   **Modular Architecture:** The project is designed with a modular architecture, allowing for easy replacement and customization of individual components. The consensus algorithm, networking layer, and smart contract execution environment can be swapped out with alternative implementations.

*   **Network Simulation:** Includes a built-in network simulator that allows for testing the consensus algorithm under various network conditions, such as latency, packet loss, and node failures. This allows researchers to evaluate the robustness of the system in realistic scenarios.

*   **State Machine Replication:** The system replicates the state of the application across all validators, ensuring data consistency and fault tolerance. The state is updated by executing smart contracts, and the consensus algorithm ensures that all validators agree on the order of execution.

*   **Event Logging and Monitoring:** Provides detailed logging and monitoring capabilities, allowing users to track the behavior of the system and identify potential issues. Metrics such as block production rate, latency, and validator performance are collected and displayed in a user-friendly format.

*   **Python-Based:** Written in Python for ease of use, prototyping, and experimentation. Python's extensive libraries and rapid prototyping capabilities make it an ideal choice for building and testing distributed systems.

## Technology Stack

*   **Python:** The core programming language used for the entire project. Provides a flexible and easy-to-use platform for developing and prototyping distributed systems.
*   **py-wasm:** A Python library for executing WASM bytecode. Used to provide a secure and sandboxed environment for running smart contracts.
*   **asyncio:** Python's built-in asynchronous I/O library. Used for handling network communication and other asynchronous tasks.
*   **json:** Used for serializing and deserializing data. Provides a simple and efficient way to represent data in a human-readable format.
*   **logging:** Python's standard logging library. Used for logging events and debugging the system.

## Installation

1.  Clone the repository:
    git clone https://github.com/jjfhwang/ConsensusForge.git

2.  Navigate to the project directory:
    cd ConsensusForge

3.  Create a virtual environment (recommended):
    python3 -m venv venv
    source venv/bin/activate

4.  Install the required dependencies:
    pip install -r requirements.txt

## Configuration

The project can be configured using environment variables. The following environment variables are supported:

*   `NODE_ID`: The unique identifier for the node. (e.g., 1, 2, 3)
*   `HOST`: The hostname or IP address of the node. (e.g., localhost, 127.0.0.1)
*   `PORT`: The port number for the node to listen on. (e.g., 8000, 8001, 8002)
*   `PEERS`: A comma-separated list of peer addresses in the format "host:port". (e.g., "localhost:8001,localhost:8002")
*   `STAKE`: The amount of stake the node has. This value must be an integer (e.g., 100, 500, 1000).

You can set these environment variables in your shell or using a `.env` file. For example:

NODE_ID=1
HOST=localhost
PORT=8000
PEERS=localhost:8001,localhost:8002
STAKE=100

## Usage

To start a node, run the `node.py` script:

python node.py

Ensure that you have set the required environment variables before running the script. For example, to start three nodes on localhost with different ports and stakes:

In terminal 1:
NODE_ID=1 HOST=localhost PORT=8000 PEERS=localhost:8001,localhost:8002 STAKE=100 python node.py

In terminal 2:
NODE_ID=2 HOST=localhost PORT=8001 PEERS=localhost:8000,localhost:8002 STAKE=500 python node.py

In terminal 3:
NODE_ID=3 HOST=localhost PORT=8002 PEERS=localhost:8000,localhost:8001 STAKE=200 python node.py

The nodes will automatically discover each other and begin participating in the consensus process. You can monitor the progress of the consensus algorithm by observing the logs printed to the console. Detailed API documentation and examples for interacting with the nodes (e.g., submitting transactions, deploying smart contracts) will be provided in future updates.

## Contributing

We welcome contributions from the community! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Adhere to the project's coding style.
*   Include unit tests for your code.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/ConsensusForge/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their contributions to the technologies used in this project.