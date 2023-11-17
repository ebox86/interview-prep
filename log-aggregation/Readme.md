# Log aggregation

This interview task typically involves writing a script to perform basic log aggregation.

For example, given the following log lines:

```
2023-11-16 21:30:12 WARNING Disk space on server 'server01' is below 10%.
2023-11-16 21:32:12 INFO System health check completed. No issues found.
2023-11-16 21:35:12 ERROR Failed to update configuration file.
```

Aggregate by log level and provide counts. 

The `format_counts` shows an example formatting and count output function

