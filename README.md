# have-I-been-pwned
Quick python script that generates a random password based on the user's desired length. Using a pseudo random number to choose an integer between the value of 33 and 146 which are the decimals of alphabets (lowercase and uppercase) as well as all the special characters in an ASCII table to generate a random password. You can then choose to check your password for data breaches using the https://haveibeenpwned.com/ API to check if your password has been breached and the number of breaches it has been involved in.

# Run
1.) To generate a random password:
```bash
    $ python -c 'import password; password.random_password()'
```
2.) To check password for breaches:
```bash
    $ python -c 'import password; password.check_password_breach()'
```

# License
[GNU General Public License v3.0](LICENSE)