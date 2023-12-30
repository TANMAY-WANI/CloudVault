# CloudVault

## Features

- **LVM and NFS Integration:** CloudVault leverages LVM for efficient volume management and NFS for remote file system access.

- **Python Command Line Interface:** Easily mount and manage storage on your local system using Python-based Linux commands.

- **Flask Web Application:** A user-friendly web interface powered by Flask allows users to interact with and manage their storage effortlessly.

- **Mount/Unmount through UI:** Perform mounting and unmounting operations conveniently through the web application.

- **Scalable Storage:** Utilize CloudVault for both personal and enterprise-level storage needs.

## Getting Started

### Prerequisites

- Linux operating system
- Python installed
- LVM configured on the system
- NFS installed and configured

### Installation

1. Clone the repository: `git clone https://github.com/TANMAY-WANI/CloudVault.git`
2. Navigate to the project directory: `cd CloudVault`
3. Install dependencies: `pip install -r requirements.txt`

### Usage

1. **Start Flask Web Application:**
   ```bash
   python app.py
   ```

2. Open your web browser and visit [http://localhost:5000](http://localhost:5000) to access the web application.

3. Use the web interface to mount and unmount storage conveniently.

## Configuration

- Edit the configuration file (`config.ini`) to set parameters such as NFS server details, default volume size, etc.

## Contributing

We welcome contributions from the community! If you'd like to contribute to CloudVault, please follow our [contribution guidelines](CONTRIBUTING.md).

## Contact

For questions or support, please contact [Tanmay Wani](mailto:tanmaywani145@gmail.com).
