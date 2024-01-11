
demo_config = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'example.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'example_logger': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}
