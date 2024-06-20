# Twilio Sub-Account Management Script

This project contains a Python script to update the status of a Twilio sub-account to "closed" and print the friendly name of the closed sub-account.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

### 1. Clone the Repository

Clone this repository to your local machine.

```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment

Create a virtual environment to manage project dependencies.

```sh
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment.

- On **Windows**:

  ```sh
  .\venv\Scripts\activate
  ```

- On **macOS and Linux**:

  ```sh
  source venv/bin/activate
  ```

### 4. Install Dependencies

Install the required packages using the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

### 5. Create a `.env` File

Create a `.env` file in the project directory and add your Twilio Account SID and Auth Token.

```plaintext
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
```

## Usage

### Running the Script

Run the script to update the status of a Twilio sub-account to "closed".

```sh
python your_script_name.py
```

### Script Functionality

1. **Prompt for Sub-Account SID**:
   The script will prompt you to enter the SID of the sub-account you want to close.

2. **Update Sub-Account Status**:
   The script will update the status of the specified sub-account to "closed".

3. **Output**:
   - If the sub-account is successfully closed, the script will output: `The subaccount {friendly_name} has been closed.`
   - If an error occurs, the script will output the error message.

## Example

```sh
Please enter the sub-account SID: ACXXXX-SUBACCOUNT-SID-XXXX
The subaccount friendly_name has been closed.
```

## Deactivate the Virtual Environment

When you are done, you can deactivate the virtual environment.

```sh
deactivate
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
