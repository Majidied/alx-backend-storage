# 0x02-redis_basic

## Description

`0x02-redis_basic` is a project that introduces the fundamentals of Redis, an open-source, in-memory data structure store used as a database, cache, and message broker. This project aims to provide a basic understanding of how to interact with Redis using Python, covering essential concepts and operations.

## Learning Objectives

- Understand the basics of Redis and its key features.
- Learn how to set up and configure a Redis server.
- Perform basic Redis operations such as setting, getting, and deleting keys.
- Explore different data types supported by Redis (strings, lists, sets, hashes, etc.).
- Implement basic caching mechanisms using Redis.
- Understand how to handle data persistence in Redis.

## Requirements

- Python 3.x
- Redis server installed and running locally or accessible remotely.
- `redis-py` library for Python Redis client.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/majidied/alx-backend-storage.git
    cd 0x02-redis_basic
    ```

2. **Install dependencies:**

    Make sure you have Python installed, then install the `redis-py` library:

    ```sh
    pip install redis
    ```

3. **Set up Redis:**

    Follow the instructions to install Redis on your machine from the [official Redis documentation](https://redis.io/download).

## Usage

1. **Starting the Redis server:**

    Make sure the Redis server is running. You can start the Redis server using the command:

    ```sh
    redis-server
    ```

2. **Running the examples:**

    The repository includes various example scripts demonstrating basic Redis operations. To run an example, use:

    ```sh
    python example_script.py
    ```

    Replace `example_script.py` with the name of the script you want to run.

## Examples

- **Basic Operations:**

    ```python
    import redis

    # Connect to Redis server
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Set a key
    r.set('foo', 'bar')

    # Get a key
    value = r.get('foo')
    print(value)  # Output: b'bar'

    # Delete a key
    r.delete('foo')
    ```

- **Using Redis as a Cache:**

    ```python
    import redis
    import time

    r = redis.Redis(host='localhost', port=6379, db=0)

    def expensive_function():
        time.sleep(2)
        return "expensive result"

    def get_cached_result():
        cached_result = r.get('cached_result')
        if cached_result:
            return cached_result.decode('utf-8')
        result = expensive_function()
        r.setex('cached_result', 10, result)  # Cache for 10 seconds
        return result

    print(get_cached_result())  # First call takes 2 seconds
    print(get_cached_result())  # Subsequent calls are instant until cache expires
    ```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to the branch.
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Redis](https://redis.io/)
- [redis-py](https://github.com/andymccurdy/redis-py)
