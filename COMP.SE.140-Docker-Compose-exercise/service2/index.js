const express = require('express');
const os = require('os');
const { execSync } = require('child_process');

const app = express();

function getSystemInfo() {
    const ipAddress = Object.values(os.networkInterfaces())
        .flat()
        .find(info => info.family === 'IPv4' && !info.internal)?.address || 'N/A';

    // Format disk space information
    const diskSpaceRaw = execSync('df -h /').toString().split('\n');
    const diskSpaceParts = diskSpaceRaw[1].split(/\s+/);  // Extract the second line (data row)
    const diskSpace = {
        "Filesystem": diskSpaceParts[0],
        "Size": diskSpaceParts[1],
        "Used": diskSpaceParts[2],
        "Available": diskSpaceParts[3],
        "Use%": diskSpaceParts[4],
        "Mounted on": diskSpaceParts[5]
    };

    // Format process information
    const processesRaw = execSync('ps -ax').toString().split('\n');
    const processes = processesRaw.slice(1).map(line => {
        const parts = line.trim().split(/\s+/, 4);  // Split each line into columns
        return {
            "PID": parts[0],
            "TTY": parts[1],
            "STAT": parts[2],
            "TIME": parts[3],
            "COMMAND": parts[4] || 'N/A'
        };
    });

    const uptime = execSync('uptime -p').toString().trim();

    return {
        "IP Address": ipAddress,
        "Processes": processes,
        "Disk Space": diskSpace,
        "Uptime": uptime
    };
}

app.get('/', (req, res) => {
    // Pretty-print the JSON with 4 spaces for indentation
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(getSystemInfo(), null, 4));
});

app.listen(5000, () => {
    console.log('Service2 (Node.js) is running on port 5000');
});
