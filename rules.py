ATTACK_RULES = {
    "SQL Injection": ["' OR 1=1", "--", "UNION SELECT"],
    "XSS": ["<script>", "</script>"],
    "Command Injection": ["cmd.exe", "powershell", "; ls"],
    "Directory Traversal": ["../", "..\\"]
}
