


Project Path: docs

Source Tree:

```txt
docs
├── README.md
├── build-docs.sh
├── markdown
│   ├── index.md
│   ├── python
│   │   ├── base_batch.md
│   │   ├── base_client.md
│   │   ├── cluster_batch.md
│   │   ├── cluster_commands.md
│   │   ├── cluster_transaction.md
│   │   ├── config.md
│   │   ├── core.md
│   │   ├── exceptions.md
│   │   ├── glide_client.md
│   │   ├── glide_cluster_client.md
│   │   ├── index.md
│   │   ├── logger.md
│   │   ├── standalone_batch.md
│   │   ├── standalone_commands.md
│   │   └── standalone_transaction.md
│   └── style.css
└── mkdocs.yml

```

`docs/README.md`:

```md
# Valkey GLIDE MkDocs Website

This directory contains everything needed to build and deploy the MkDocs-based documentation site hosted on Valkey GLIDE's GitHub Pages.

## How It Works

The documentation is built and deployed using the [`./build-docs.sh`](./build-docs.sh) script.

- **Python documentation** is generated using the [`mkdocstrings`](https://mkdocstrings.github.io/) plugin for MkDocs. See more about the Python documentation [here](https://github.com/valkey-io/valkey-glide/blob/main/python/DEVELOPER.md#documentation).
- **Node.js documentation** is generated using [`TypeDoc`](https://typedoc.org/), which produces Markdown files that are then processed by MkDocs.

## Building and Serving Locally

To **build** the site locally, run the following from the `docs` directory:

```bash
./build-docs.sh build
```

To **build and serve** the site locally (deploy to localhost), run the following from the `docs` directory:
```bash
./build-docs.sh serve
```

## Community Support and Feedback

We encourage you to join our community to support, share feedback, and ask questions. You can approach us for anything on our Valkey Slack: [Join Valkey Slack](https://join.slack.com/t/valkey-oss-developer/shared_invite/zt-2nxs51chx-EB9hu9Qdch3GMfRcztTSkQ).

```

`docs/build-docs.sh`:

```sh
#!/bin/bash -ex

TARGET=$@
if [ -z "$TARGET" ]; then
    TARGET="build"
fi

BASE_DIR=$(readlink -f $(dirname $(readlink -f $0))/..)

# For building the docs, we require mkdocs + mkdocstrings-python
function install_mkdocs() {
    if ! command -v mkdocs >/dev/null 2>&1; then
        echo "-- Installing mkdocs ..."
        pip3 install --upgrade pip
        pip3 install                           \
            mkdocs                             \
            mkdocstrings-python==1.13.0        \
            pymdown-extensions                 \
            mkdocs-breadcrumbs-plugin          \
            mkdocs-material
        echo "-- Done"
    fi
    command -v mkdocs
}

function build_docs() {
    # NodeJS
    (cd ${BASE_DIR}/node && npm run docs)

    # Python - should be last, since Python docs are generated using mkdocs plugin
    # Set PYTHONPATH so python classes are found
    export PYTHONPATH=${BASE_DIR}/python/python:$PYTHONPATH
    (cd ${BASE_DIR}/docs && python3 -m mkdocs ${TARGET})
}

install_mkdocs
build_docs $@

```

`docs/markdown/index.md`:

```md
# Valkey GLIDE

Valkey General Language Independent Driver for the Enterprise (GLIDE), is an open-source Valkey client library. Valkey GLIDE is one of the official client libraries for Valkey, and it supports all Valkey commands. Valkey GLIDE supports Valkey 7.2 and above, and Redis open-source 6.2, 7.0 and 7.2. Application programmers use Valkey GLIDE to safely and reliably connect their applications to Valkey- and Redis OSS- compatible services. Valkey GLIDE is designed for reliability, optimized performance, and high-availability, for Valkey and Redis OSS based applications. It is sponsored and supported by AWS, and is pre-configured with best practices learned from over a decade of operating Redis OSS-compatible services used by hundreds of thousands of customers. To help ensure consistency in application development and operations, Valkey GLIDE is implemented using a core driver framework, written in Rust, with language specific extensions. This design ensures consistency in features across languages and reduces overall complexity.

## Supported Engine Versions

Refer to the [Supported Engine Versions table](https://github.com/valkey-io/valkey-glide/blob/main/README.md#supported-engine-versions) for details.

## System Requirements

The release of Valkey GLIDE was tested on the following platforms:

Linux:

-   Ubuntu 22.04.1 (x86_64 and aarch64)
-   Amazon Linux 2023 (AL2023) (x86_64)

macOS:

-   macOS 14.7 (Apple silicon/aarch_64)

## Installation and Setup

=== "Python"
    To install Valkey GLIDE using `pip`, follow these steps:

    1. Open your terminal.
    2. Execute the command below:
    ```bash
    $ pip install valkey-glide
    ```
    3. After installation, confirm the client is accessible by running:
    ```bash
    $ python3
    >>> import glide
    ```

=== "TypeScript"
    use `npm` to install:

    ```bash
    npm i @valkey/valkey-glide
    ```

## Basic Examples

=== "Python"
    === "Standalone Mode"

        ```python
        import asyncio
        from glide import GlideClientConfiguration, NodeAddress, GlideClient
        async def test_standalone_client():
            addresses = [
                    NodeAddress("server_primary.example.com", 6379),
                    NodeAddress("server_replica.example.com", 6379)
            ]
            config = GlideClientConfiguration(addresses)
            client = await GlideClient.create(config)
            set_result = await client.set("foo", "bar")
            print(f"Set response is {set_result}")
            get_result = await client.get("foo")
            print(f"Get response is {get_result}")

        asyncio.run(test_standalone_client())
        ```

        Output:

        ```text
        Set response is OK
        Get response is bar
        ```

    === "Cluster Mode"
        ```python
        import asyncio
        from glide import GlideClusterClientConfiguration, NodeAddress, GlideClusterClient
        async def test_cluster_client():
            addresses = [NodeAddress("address.example.com", 6379)]
            config = GlideClusterClientConfiguration(addresses)
            client = await GlideClusterClient.create(config)
            set_result = await client.set("foo", "bar")
            print(f"Set response is {set_result}")
            get_result = await client.get("foo")
            print(f"Get response is {get_result}")

        asyncio.run(test_cluster_client())
        ```

        Output:

        ```text
        Set response is OK
        Get response is bar
        ```

=== "TypeScript"

    === "Standalone Mode"

        ```typescript
        import { GlideClient, GlideClusterClient, Logger } from "@valkey/valkey-glide";
        // When Valkey is in standalone mode, add address of the primary node, and any replicas you'd like to be able to read from.
        const addresses = [
            {
                host: "localhost",
                port: 6379,
            },
        ];
        // Check `GlideClientConfiguration/GlideClusterClientConfiguration` for additional options.
        const client = await GlideClient.createClient({
            addresses: addresses,
            // if the server uses TLS, you'll need to enable it. Otherwise, the connection attempt will time out silently.
            // useTLS: true,
            clientName: "test_standalone_client",
        });
        // The empty array signifies that there are no additional arguments.
        const pong = await client.customCommand(["PING"]);
        console.log(pong);
        const set_response = await client.set("foo", "bar");
        console.log(`Set response is = ${set_response}`);
        const get_response = await client.get("foo");
        console.log(`Get response is = ${get_response}`);
        ```

    === "Cluster Mode"

        ```typescript
        import { GlideClient, GlideClusterClient, Logger } from "@valkey/valkey-glide";
        // When Valkey is in cluster mode, add address of any nodes, and the client will find all nodes in the cluster.
        const addresses = [
            {
                host: "localhost",
                port: 6379,
            },
        ];
        // Check `GlideClientConfiguration/GlideClusterClientConfiguration` for additional options.
        const client = await GlideClusterClient.createClient({
            addresses: addresses,
            // if the cluster nodes use TLS, you'll need to enable it. Otherwise the connection attempt will time out silently.
            // useTLS: true,
            clientName: "test_cluster_client",
        });
        // The empty array signifies that there are no additional arguments.
        const pong = await client.customCommand(["PING"], { route: "randomNode" });
        console.log(pong);
        const set_response = await client.set("foo", "bar");
        console.log(`Set response is = ${set_response}`);
        const get_response = await client.get("foo");
        console.log(`Get response is = ${get_response}`);
        client.close();
        ```


## References

=== "Python"
    - [Python standalone example][1]
    - [Python cluster example][2]
    - [Python wiki for examples and further details on TLS, Read strategy, Timeouts and various other configurations][3]

=== "TypeScript"
    - [TypeScript standalone example][5]
    - [TypeScript cluster example][6]
    - [TypeScript wiki for examples and further details on TLS, Read strategy, Timeouts and various other configurations][4]

[1]: https://github.com/valkey-io/valkey-glide/blob/main/examples/python/standalone_example.py
[2]: https://github.com/valkey-io/valkey-glide/blob/main/examples/python/cluster_example.py
[3]: https://github.com/valkey-io/valkey-glide/wiki/Python-wrapper
[4]: https://github.com/valkey-io/valkey-glide/wiki/NodeJS-wrapper
[5]: https://github.com/valkey-io/valkey-glide/blob/main/examples/node/standalone_example.ts
[6]: https://github.com/valkey-io/valkey-glide/blob/main/examples/node/cluster_example.ts

```

`docs/markdown/python/base_batch.md`:

```md
::: glide.async_commands.batch.BaseBatch

```

`docs/markdown/python/base_client.md`:

```md
::: glide.glide_client.BaseClient

```

`docs/markdown/python/cluster_batch.md`:

```md
::: glide.async_commands.batch.ClusterBatch

```

`docs/markdown/python/cluster_commands.md`:

```md
::: glide.async_commands.cluster_commands.ClusterCommands

```

`docs/markdown/python/cluster_transaction.md`:

```md
::: glide.async_commands.batch.ClusterTransaction

```

`docs/markdown/python/config.md`:

```md
::: glide.config.GlideClientConfiguration
::: glide.config.GlideClusterClientConfiguration
::: glide.config.NodeAddress
::: glide.config.ReadFrom
::: glide.config.ProtocolVersion
::: glide.config.BackoffStrategy
::: glide.config.ServerCredentials
::: glide.config.PeriodicChecksManualInterval
::: glide.config.PeriodicChecksStatus
::: glide.config.BaseClientConfiguration

```

`docs/markdown/python/core.md`:

```md
::: glide.async_commands.CoreCommands
::: glide.async_commands.core.ConditionalChange
::: glide.async_commands.core.ExpiryType
::: glide.async_commands.core.ExpiryTypeGetEx
::: glide.async_commands.core.InfoSection
::: glide.async_commands.core.ExpireOptions
::: glide.async_commands.core.UpdateOptions
::: glide.async_commands.core.ExpirySet
::: glide.async_commands.core.ExpiryGetEx
::: glide.async_commands.core.InsertPosition
::: glide.async_commands.core.FlushMode
::: glide.async_commands.core.FunctionRestorePolicy

```

`docs/markdown/python/exceptions.md`:

```md
::: glide.exceptions.GlideError
::: glide.exceptions.ClosingError
::: glide.exceptions.RequestError
::: glide.exceptions.TimeoutError
::: glide.exceptions.ExecAbortError
::: glide.exceptions.ConnectionError
::: glide.exceptions.ConfigurationError

```

`docs/markdown/python/glide_client.md`:

```md
::: glide.glide_client.GlideClient
::: glide.glide_client.BaseClient

```

`docs/markdown/python/glide_cluster_client.md`:

```md
::: glide.glide_client.GlideClusterClient
::: glide.glide_client.BaseClient

```

`docs/markdown/python/index.md`:

```md
# Index of python

- [base_client](/valkey-glide/python/base_client/)
- [base_transaction](/valkey-glide/python/base_transaction/)
- [cluster_commands](/valkey-glide/python/cluster_commands/)
- [cluster_transaction](/valkey-glide/python/cluster_transaction/)
- [config](/valkey-glide/python/config/)
- [core](/valkey-glide/python/core/)
- [exceptions](/valkey-glide/python/exceptions/)
- [glide_client](/valkey-glide/python/glide_client/)
- [glide_cluster_client](/valkey-glide/python/glide_cluster_client/)
- [standalone_command](/valkey-glide/python/standalone_command/)
- [standalone_transaction](/valkey-glide/python/standalone_transaction/)
```

`docs/markdown/python/logger.md`:

```md
::: glide.logger.Logger

```

`docs/markdown/python/standalone_batch.md`:

```md
::: glide.async_commands.batch.Batch

```

`docs/markdown/python/standalone_commands.md`:

```md
::: glide.async_commands.standalone_commands.StandaloneCommands

```

`docs/markdown/python/standalone_transaction.md`:

```md
::: glide.async_commands.batch.Transaction

```

`docs/markdown/style.css`:

```css
[data-md-color-scheme="valkey-glide"] {
    --md-primary-fg-color: #7189ff;
}

```

`docs/mkdocs.yml`:

```yml
site_name: GLIDE for Valkey - API Documentation
site_url: https://valkey.io/valkey-glide
repo_url: https://github.com/valkey-io/valkey-glide
repo_name: GitHub
docs_dir: markdown
nav:
  - Python:
      - Client:
          - Standalone: python/glide_client.md
          - Cluster: python/glide_cluster_client.md
          - Base: python/base_client.md
      - Config: python/config.md
      - Commands:
          - Core Commands: python/core.md
          - Cluster Commands: python/cluster_commands.md
          - Standalone Commands: python/standalone_commands.md
          - Base Batch: python/base_batch.md
          - Standalone Batch: python/standalone_batch.md
          - Cluster Batch: python/cluster_batch.md
          - Standalone Transaction (Deprecated): python/standalone_transaction.md
          - Cluster Transaction (Deprecated): python/cluster_transaction.md
      - Exceptions: python/exceptions.md
      - Logger: python/logger.md
  - TypeScript:
      - Client and Commands:
          - Standalone: node/GlideClient/classes/GlideClient.md
          - Cluster: node/GlideClusterClient/classes/GlideClusterClient.md
          - Base: node/BaseClient/classes/BaseClient.md
          - Base Batch: node/Batch/classes/BaseBatch.md
          - Standalone Batch: node/Batch/classes/Batch.md
          - Cluster Batch: node/Batch/classes/ClusterBatch.md
          - Transaction (Deprecated): node/Batch/classes/Transaction.md
          - Cluster Transaction (Deprecated): node/Batch/classes/ClusterTransaction.md
      - config: node/BaseClient/interfaces/BaseClientConfiguration.md
      - Modules:
          - JSON: node/server-modules/GlideJson/classes/GlideJson.md
          - Vector Search: node/server-modules/GlideFt/classes/GlideFt.md
      - Errors:
          - ClosingError: node/Errors/classes/ClosingError.md
          - ConfigurationError: node/Errors/classes/ConfigurationError.md
          - ConnectionError: node/Errors/classes/ConnectionError.md
          - ExecAbortError: node/Errors/classes/ExecAbortError.md
          - RequestError: node/Errors/classes/RequestError.md
          - TimeoutError: node/Errors/classes/TimeoutError.md
          - ValkeyError: node/Errors/classes/ValkeyError.md
      - Logger: node/Logger/classes/Logger.md
theme:
  name: material
  palette:
    scheme: valkey-glide
  features:
    - navigation.sections
    - content.code.copy
    - navigation.path
    - navigation.footer
    - navigation.top
  highlightjs: true
  font:
    text: Roboto
    code: Roboto Mono
markdown_extensions:
  - pymdownx.keys
  - admonition
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            show_symbol_type_heading: true
            show_symbol_type_toc: true
            show_root_heading: true
  - search
  - mkdocs-breadcrumbs-plugin:
      delimiter: " / " # separator between sections
      log_level: "CRITICAL" # "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
      exclude_paths:
        - "docs/mkdocs/**"
        - "docs/mkdocs" # avoid generating index.md
      additional_index_folders:
        - temp_dir
      generate_home_index: false
extra:
  generator: false
extra_css:
  - style.css

```

├── README.md
├── clients
    └── README.md
├── commands
    ├── acl-cat.md
    ├── acl-deluser.md
    ├── acl-dryrun.md
    ├── acl-genpass.md
    ├── acl-getuser.md
    ├── acl-help.md
    ├── acl-list.md
    ├── acl-load.md
    ├── acl-log.md
    ├── acl-save.md
    ├── acl-setuser.md
    ├── acl-users.md
    ├── acl-whoami.md
    ├── acl.md
    ├── append.md
    ├── asking.md
    ├── auth.md
    ├── bf.add.md
    ├── bf.card.md
    ├── bf.exists.md
    ├── bf.info.md
    ├── bf.insert.md
    ├── bf.load.md
    ├── bf.madd.md
    ├── bf.mexists.md
    ├── bf.reserve.md
    ├── bgrewriteaof.md
    ├── bgsave.md
    ├── bitcount.md
    ├── bitfield.md
    ├── bitfield_ro.md
    ├── bitop.md
    ├── bitpos.md
    ├── blmove.md
    ├── blmpop.md
    ├── blpop.md
    ├── brpop.md
    ├── brpoplpush.md
    ├── bzmpop.md
    ├── bzpopmax.md
    ├── bzpopmin.md
    ├── client-caching.md
    ├── client-capa.md
    ├── client-getname.md
    ├── client-getredir.md
    ├── client-help.md
    ├── client-id.md
    ├── client-import-source.md
    ├── client-info.md
    ├── client-kill.md
    ├── client-list.md
    ├── client-no-evict.md
    ├── client-no-touch.md
    ├── client-pause.md
    ├── client-reply.md
    ├── client-setinfo.md
    ├── client-setname.md
    ├── client-tracking.md
    ├── client-trackinginfo.md
    ├── client-unblock.md
    ├── client-unpause.md
    ├── client.md
    ├── cluster-addslots.md
    ├── cluster-addslotsrange.md
    ├── cluster-bumpepoch.md
    ├── cluster-count-failure-reports.md
    ├── cluster-countkeysinslot.md
    ├── cluster-delslots.md
    ├── cluster-delslotsrange.md
    ├── cluster-failover.md
    ├── cluster-flushslots.md
    ├── cluster-forget.md
    ├── cluster-getkeysinslot.md
    ├── cluster-help.md
    ├── cluster-info.md
    ├── cluster-keyslot.md
    ├── cluster-links.md
    ├── cluster-meet.md
    ├── cluster-myid.md
    ├── cluster-myshardid.md
    ├── cluster-nodes.md
    ├── cluster-replicas.md
    ├── cluster-replicate.md
    ├── cluster-reset.md
    ├── cluster-saveconfig.md
    ├── cluster-set-config-epoch.md
    ├── cluster-setslot.md
    ├── cluster-shards.md
    ├── cluster-slaves.md
    ├── cluster-slot-stats.md
    ├── cluster-slots.md
    ├── cluster.md
    ├── command-count.md
    ├── command-docs.md
    ├── command-getkeys.md
    ├── command-getkeysandflags.md
    ├── command-help.md
    ├── command-info.md
    ├── command-list.md
    ├── command.md
    ├── commandlog-get.md
    ├── commandlog-help.md
    ├── commandlog-len.md
    ├── commandlog-reset.md
    ├── commandlog.md
    ├── config-get.md
    ├── config-help.md
    ├── config-resetstat.md
    ├── config-rewrite.md
    ├── config-set.md
    ├── config.md
    ├── copy.md
    ├── dbsize.md
    ├── debug.md
    ├── decr.md
    ├── decrby.md
    ├── del.md
    ├── discard.md
    ├── dump.md
    ├── echo.md
    ├── eval.md
    ├── eval_ro.md
    ├── evalsha.md
    ├── evalsha_ro.md
    ├── exec.md
    ├── exists.md
    ├── expire.md
    ├── expireat.md
    ├── expiretime.md
    ├── failover.md
    ├── fcall.md
    ├── fcall_ro.md
    ├── flushall.md
    ├── flushdb.md
    ├── function-delete.md
    ├── function-dump.md
    ├── function-flush.md
    ├── function-help.md
    ├── function-kill.md
    ├── function-list.md
    ├── function-load.md
    ├── function-restore.md
    ├── function-stats.md
    ├── function.md
    ├── geoadd.md
    ├── geodist.md
    ├── geohash.md
    ├── geopos.md
    ├── georadius.md
    ├── georadius_ro.md
    ├── georadiusbymember.md
    ├── georadiusbymember_ro.md
    ├── geosearch.md
    ├── geosearchstore.md
    ├── get.md
    ├── getbit.md
    ├── getdel.md
    ├── getex.md
    ├── getrange.md
    ├── getset.md
    ├── hdel.md
    ├── hello.md
    ├── hexists.md
    ├── hget.md
    ├── hgetall.md
    ├── hincrby.md
    ├── hincrbyfloat.md
    ├── hkeys.md
    ├── hlen.md
    ├── hmget.md
    ├── hmset.md
    ├── hrandfield.md
    ├── hscan.md
    ├── hset.md
    ├── hsetnx.md
    ├── hstrlen.md
    ├── hvals.md
    ├── incr.md
    ├── incrby.md
    ├── incrbyfloat.md
    ├── info.md
    ├── json.arrappend.md
    ├── json.arrindex.md
    ├── json.arrinsert.md
    ├── json.arrlen.md
    ├── json.arrpop.md
    ├── json.arrtrim.md
    ├── json.clear.md
    ├── json.debug.md
    ├── json.del.md
    ├── json.forget.md
    ├── json.get.md
    ├── json.mget.md
    ├── json.mset.md
    ├── json.numincrby.md
    ├── json.nummultby.md
    ├── json.objkeys.md
    ├── json.objlen.md
    ├── json.resp.md
    ├── json.set.md
    ├── json.strappend.md
    ├── json.strlen.md
    ├── json.toggle.md
    ├── json.type.md
    ├── keys.md
    ├── lastsave.md
    ├── latency-doctor.md
    ├── latency-graph.md
    ├── latency-help.md
    ├── latency-histogram.md
    ├── latency-history.md
    ├── latency-latest.md
    ├── latency-reset.md
    ├── latency.md
    ├── lcs.md
    ├── lindex.md
    ├── linsert.md
    ├── llen.md
    ├── lmove.md
    ├── lmpop.md
    ├── lolwut.md
    ├── lpop.md
    ├── lpos.md
    ├── lpush.md
    ├── lpushx.md
    ├── lrange.md
    ├── lrem.md
    ├── lset.md
    ├── ltrim.md
    ├── memory-doctor.md
    ├── memory-help.md
    ├── memory-malloc-stats.md
    ├── memory-purge.md
    ├── memory-stats.md
    ├── memory-usage.md
    ├── memory.md
    ├── mget.md
    ├── migrate.md
    ├── module-help.md
    ├── module-list.md
    ├── module-load.md
    ├── module-loadex.md
    ├── module-unload.md
    ├── module.md
    ├── monitor.md
    ├── move.md
    ├── mset.md
    ├── msetnx.md
    ├── multi.md
    ├── object-encoding.md
    ├── object-freq.md
    ├── object-help.md
    ├── object-idletime.md
    ├── object-refcount.md
    ├── object.md
    ├── persist.md
    ├── pexpire.md
    ├── pexpireat.md
    ├── pexpiretime.md
    ├── pfadd.md
    ├── pfcount.md
    ├── pfdebug.md
    ├── pfmerge.md
    ├── pfselftest.md
    ├── ping.md
    ├── psetex.md
    ├── psubscribe.md
    ├── psync.md
    ├── pttl.md
    ├── publish.md
    ├── pubsub-channels.md
    ├── pubsub-help.md
    ├── pubsub-numpat.md
    ├── pubsub-numsub.md
    ├── pubsub-shardchannels.md
    ├── pubsub-shardnumsub.md
    ├── pubsub.md
    ├── punsubscribe.md
    ├── quit.md
    ├── randomkey.md
    ├── readonly.md
    ├── readwrite.md
    ├── rename.md
    ├── renamenx.md
    ├── replconf.md
    ├── replicaof.md
    ├── reset.md
    ├── restore-asking.md
    ├── restore.md
    ├── role.md
    ├── rpop.md
    ├── rpoplpush.md
    ├── rpush.md
    ├── rpushx.md
    ├── sadd.md
    ├── save.md
    ├── scan.md
    ├── scard.md
    ├── script-debug.md
    ├── script-exists.md
    ├── script-flush.md
    ├── script-help.md
    ├── script-kill.md
    ├── script-load.md
    ├── script-show.md
    ├── script.md
    ├── sdiff.md
    ├── sdiffstore.md
    ├── select.md
    ├── set.md
    ├── setbit.md
    ├── setex.md
    ├── setnx.md
    ├── setrange.md
    ├── shutdown.md
    ├── sinter.md
    ├── sintercard.md
    ├── sinterstore.md
    ├── sismember.md
    ├── slaveof.md
    ├── slowlog-get.md
    ├── slowlog-help.md
    ├── slowlog-len.md
    ├── slowlog-reset.md
    ├── slowlog.md
    ├── smembers.md
    ├── smismember.md
    ├── smove.md
    ├── sort.md
    ├── sort_ro.md
    ├── spop.md
    ├── spublish.md
    ├── srandmember.md
    ├── srem.md
    ├── sscan.md
    ├── ssubscribe.md
    ├── strlen.md
    ├── subscribe.md
    ├── substr.md
    ├── sunion.md
    ├── sunionstore.md
    ├── sunsubscribe.md
    ├── swapdb.md
    ├── sync.md
    ├── time.md
    ├── touch.md
    ├── ttl.md
    ├── type.md
    ├── unlink.md
    ├── unsubscribe.md
    ├── unwatch.md
    ├── wait.md
    ├── waitaof.md
    ├── watch.md
    ├── xack.md
    ├── xadd.md
    ├── xautoclaim.md
    ├── xclaim.md
    ├── xdel.md
    ├── xgroup-create.md
    ├── xgroup-createconsumer.md
    ├── xgroup-delconsumer.md
    ├── xgroup-destroy.md
    ├── xgroup-help.md
    ├── xgroup-setid.md
    ├── xgroup.md
    ├── xinfo-consumers.md
    ├── xinfo-groups.md
    ├── xinfo-help.md
    ├── xinfo-stream.md
    ├── xinfo.md
    ├── xlen.md
    ├── xpending.md
    ├── xrange.md
    ├── xread.md
    ├── xreadgroup.md
    ├── xrevrange.md
    ├── xsetid.md
    ├── xtrim.md
    ├── zadd.md
    ├── zcard.md
    ├── zcount.md
    ├── zdiff.md
    ├── zdiffstore.md
    ├── zincrby.md
    ├── zinter.md
    ├── zintercard.md
    ├── zinterstore.md
    ├── zlexcount.md
    ├── zmpop.md
    ├── zmscore.md
    ├── zpopmax.md
    ├── zpopmin.md
    ├── zrandmember.md
    ├── zrange.md
    ├── zrangebylex.md
    ├── zrangebyscore.md
    ├── zrangestore.md
    ├── zrank.md
    ├── zrem.md
    ├── zremrangebylex.md
    ├── zremrangebyrank.md
    ├── zremrangebyscore.md
    ├── zrevrange.md
    ├── zrevrangebylex.md
    ├── zrevrangebyscore.md
    ├── zrevrank.md
    ├── zscan.md
    ├── zscore.md
    ├── zunion.md
    └── zunionstore.md
├── resources
    ├── clients
    │   └── index.md
    ├── libraries
    │   └── index.md
    ├── modules
    │   └── index.md
    └── tools
    │   └── index.md
└── topics
    ├── ARM.md
    ├── RDMA.md
    ├── acl.md
    ├── admin.md
    ├── benchmark.md
    ├── bitfields.md
    ├── bitmaps.md
    ├── bloomfilters.md
    ├── cli.md
    ├── client-side-caching.md
    ├── clients.md
    ├── cluster-spec.md
    ├── cluster-tutorial.md
    ├── command-arguments.md
    ├── command-tips.md
    ├── data-types.md
    ├── debugging.md
    ├── distlock.md
    ├── encryption.md
    ├── eval-intro.md
    ├── faq.md
    ├── functions-intro.md
    ├── geospatial.md
    ├── hashes.md
    ├── history.md
    ├── hyperloglogs.md
    ├── index.md
    ├── indexing.md
    ├── installation.md
    ├── introduction.md
    ├── key-specs.md
    ├── keyspace.md
    ├── latency-monitor.md
    ├── latency.md
    ├── ldb.md
    ├── license.md
    ├── lists.md
    ├── lru-cache.md
    ├── lua-api.md
    ├── mass-insertion.md
    ├── memory-optimization.md
    ├── migration.md
    ├── modules-api-ref.md
    ├── modules-blocking-ops.md
    ├── modules-intro.md
    ├── modules-native-types.md
    ├── notifications.md
    ├── performance-on-cpu.md
    ├── persistence.md
    ├── pipelining.md
    ├── problems.md
    ├── programmability.md
    ├── protocol.md
    ├── pubsub.md
    ├── quickstart.md
    ├── releases.md
    ├── replication.md
    ├── security.md
    ├── sentinel-clients.md
    ├── sentinel.md
    ├── server.md
    ├── sets.md
    ├── signals.md
    ├── sorted-sets.md
    ├── streams-intro.md
    ├── strings.md
    ├── transactions.md
    ├── twitter-clone.md
    ├── valkey-json.md
    └── valkey.conf.md


/commands/acl-deluser.md:
--------------------------------------------------------------------------------
 1 | Delete all the specified ACL users and terminate all the connections that are
 2 | authenticated with such users. Note: the special `default` user cannot be
 3 | removed from the system, this is the default user that every new connection
 4 | is authenticated with. The list of users may include usernames that do not
 5 | exist, in such case no operation is performed for the non existing users.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> ACL DELUSER antirez
11 | (integer) 1
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/acl-dryrun.md:
--------------------------------------------------------------------------------
 1 | Simulate the execution of a given command by a given user.
 2 | This command can be used to test the permissions of a given user without having to enable the user or cause the side effects of running the command.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> ACL SETUSER VIRGINIA +SET ~*
 8 | "OK"
 9 | 127.0.0.1:6379> ACL DRYRUN VIRGINIA SET foo bar
10 | "OK"
11 | 127.0.0.1:6379> ACL DRYRUN VIRGINIA GET foo
12 | "User VIRGINIA has no permissions to run the 'get' command"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/acl-help.md:
--------------------------------------------------------------------------------
1 | The `ACL HELP` command returns a helpful text describing the different subcommands.
2 |
3 |


--------------------------------------------------------------------------------
/commands/acl-list.md:
--------------------------------------------------------------------------------
 1 | The command shows the currently active ACL rules in the Valkey server. Each
 2 | line in the returned array defines a different user, and the format is the
 3 | same used in the valkey.conf file or the external ACL file, so you can
 4 | cut and paste what is returned by the ACL LIST command directly inside a
 5 | configuration file if you wish (but make sure to check `ACL SAVE`).
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> ACL LIST
11 | 1) "user antirez on #9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 ~objects:* &* +@all -@admin -@dangerous"
12 | 2) "user default on nopass ~* &* +@all"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/acl-load.md:
--------------------------------------------------------------------------------
 1 | When Valkey is configured to use an ACL file (with the `aclfile` configuration
 2 | option), this command will reload the ACLs from the file, replacing all
 3 | the current ACL rules with the ones defined in the file. The command makes
 4 | sure to have an *all or nothing* behavior, that is:
 5 |
 6 | * If every line in the file is valid, all the ACLs are loaded.
 7 | * If one or more line in the file is not valid, nothing is loaded, and the old ACL rules defined in the server memory continue to be used.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> ACL LOAD
13 | OK
14 | ```
15 |
16 | ```
17 | 127.0.0.1:6379> ACL LOAD
18 | (error) ERR /tmp/foo:1: Unknown command or category name in ACL...
19 | ```
20 |


--------------------------------------------------------------------------------
/commands/acl-save.md:
--------------------------------------------------------------------------------
 1 | When Valkey is configured to use an ACL file (with the `aclfile` configuration
 2 | option), this command will save the currently defined ACLs from the server memory to the ACL file.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> ACL SAVE
 8 | OK
 9 | 127.0.0.1:6379> ACL SAVE
10 | (error) ERR There was an error trying to save the ACLs. Please check the server logs for more information
11 | ```
12 |


--------------------------------------------------------------------------------
/commands/acl-users.md:
--------------------------------------------------------------------------------
 1 | The command shows a list of all the usernames of the currently configured
 2 | users in the Valkey ACL system.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> ACL USERS
 8 | 1) "anna"
 9 | 2) "antirez"
10 | 3) "default"
11 | ```
12 |


--------------------------------------------------------------------------------
/commands/acl-whoami.md:
--------------------------------------------------------------------------------
 1 | Return the username the current connection is authenticated with.
 2 | New connections are authenticated with the "default" user. They
 3 | can change user using `AUTH`.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> ACL WHOAMI
 9 | "default"
10 | ```
11 |


--------------------------------------------------------------------------------
/commands/acl.md:
--------------------------------------------------------------------------------
1 | This is a container command for [Access Control List](../topics/acl.md) commands.
2 |
3 | To see the list of available commands you can call `ACL HELP`.
4 |


--------------------------------------------------------------------------------
/commands/asking.md:
--------------------------------------------------------------------------------
1 | When a cluster client receives an `-ASK` redirect, the `ASKING` command is sent to the target node followed by the command which was redirected.
2 | This is normally done automatically by cluster clients.
3 |
4 | If an `-ASK` redirect is received during a transaction, only one ASKING command needs to be sent to the target node before sending the complete transaction to the target node.
5 |
6 | See [ASK redirection in the Valkey Cluster Specification](../topics/cluster-spec.md#ask-redirection) for details.
7 |


--------------------------------------------------------------------------------
/commands/auth.md:
--------------------------------------------------------------------------------
 1 | The AUTH command authenticates the current connection using the [Valkey ACL system](../topics/acl.md).
 2 |
 3 | The standard way to `AUTH` is the two-argument form:
 4 |
 5 |     AUTH <username> <password>
 6 |
 7 | This authenticates the current connection with one of the users
 8 | defined in the ACL list (see `ACL SETUSER` and the official [ACL guide](../topics/acl.md) for more information).
 9 |
10 | When the single argument form of the command is used, where only the password is specified,
11 | it is assumed that the implicit username is "default".
12 |
13 |     AUTH <password>
14 |
15 | This form authenticates against the "default" user's password set with `requirepass`.
16 |
17 | If the password provided via AUTH matches the password in the configuration file, the server replies with the `OK` status code and starts accepting commands.
18 | Otherwise, an error is returned and the clients needs to try a new password.
19 |
20 | ## Security notice
21 |
22 | Because of the high performance nature of Valkey, it is possible to try
23 | a lot of passwords in parallel in very short time, so make sure to generate a
24 | strong and very long password so that this attack is infeasible.
25 | A good way to generate strong passwords is via the `ACL GENPASS` command.
26 |


--------------------------------------------------------------------------------
/commands/bf.add.md:
--------------------------------------------------------------------------------
 1 | Adds a single item to a bloom filter. If the specified bloom filter does not exist, a bloom filter is created with the provided name with default properties.
 2 |
 3 | To add multiple items to a bloom filter, you can use the `BF.MADD` or `BF.INSERT` commands.
 4 |
 5 | To create a bloom filter with non-default properties, use the `BF.INSERT` or `BF.RESERVE` command.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> BF.ADD key val
11 | (integer) 1
12 | 127.0.0.1:6379> BF.ADD key val
13 | (integer) 0
14 | ```
15 |


--------------------------------------------------------------------------------
/commands/bf.card.md:
--------------------------------------------------------------------------------
 1 | Returns the cardinality of a bloom filter which is the number of items that have been successfully added to it.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> BF.ADD key val
 7 | (integer) 1
 8 | 127.0.0.1:6379> BF.CARD key
 9 | (integer) 1
10 | 127.0.0.1:6379> BF.CARD nonexistentkey
11 | (integer) 0
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/bf.exists.md:
--------------------------------------------------------------------------------
 1 | Determines if an item has been added to the bloom filter previously.
 2 |
 3 | A bloom filter has two possible responses when you check if an item exists:
 4 |
 5 | * 0 - The item definitely does not exist since with bloom filters, false negatives are not possible.
 6 |
 7 | * 1 - The item exists with a given false positive (`fp`) percentage. There is an `fp` rate % chance that the item does not exist. You can create bloom filters with a more strict false positive rate as needed.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> BF.ADD key val
13 | (integer) 1
14 | 127.0.0.1:6379> BF.EXISTS key val
15 | (integer) 1
16 | 127.0.0.1:6379> BF.EXISTS key nonexistent
17 | (integer) 0
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/bf.load.md:
--------------------------------------------------------------------------------
1 | Restores a bloom filter from a dump of an existing bloom filter with all of its specific the properties and bit vector dump of sub filter/s. This command is only generated during AOF rewrite to restore a bloom filter in the future.
2 |


--------------------------------------------------------------------------------
/commands/bf.madd.md:
--------------------------------------------------------------------------------
 1 | Adds one or more items to a bloom filter. If the specified bloom filter does not exist, a bloom filter is created with the provided name with default properties.
 2 |
 3 | If you want to create a bloom filter with non-default properties, use the `BF.INSERT` or `BF.RESERVE` command.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> BF.MADD key item1 item2
 9 | 1) (integer) 1
10 | 2) (integer) 1
11 | 127.0.0.1:6379> BF.MADD key item2 item3
12 | 1) (integer) 0
13 | 2) (integer) 1
14 | 127.0.0.1:6379> BF.MADD key_new item1
15 | 1) (integer) 1
16 | ```


--------------------------------------------------------------------------------
/commands/bf.mexists.md:
--------------------------------------------------------------------------------
 1 | Determines if the provided item/s have been added to a bloom filter previously.
 2 |
 3 | A Bloom filter has two possible responses when you check if an item exists:
 4 |
 5 | * 0 - The item definitely does not exist since with bloom filters, false negatives are not possible.
 6 |
 7 | * 1 - The item exists with a given false positive (`fp`) percentage. There is an `fp` rate % chance that the item does not exist. You can create bloom filters with a more strict false positive rate as needed.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> BF.MADD key item1 item2
13 | 1) (integer) 1
14 | 2) (integer) 1
15 | 127.0.0.1:6379> BF.MEXISTS key item1 item2 item3
16 | 1) (integer) 1
17 | 2) (integer) 1
18 | 3) (integer) 0
19 | 127.0.0.1:6379> BF.MEXISTS key item1
20 | 1) (integer) 1
21 | ```


--------------------------------------------------------------------------------
/commands/bf.reserve.md:
--------------------------------------------------------------------------------
 1 | Creates an empty bloom filter with the specified capacity and false positive rate. By default, a scaling filter is created with the default expansion rate.
 2 |
 3 | To specify the scaling / non scaling nature of the bloom filter, use the options: `NONSCALING` or `SCALING <expansion rate>`. It is invalid to provide both options together.
 4 |
 5 | ## Reserve fields
 6 |
 7 | * error_rate - The false positive rate of the bloom filter
 8 | * capacity -  The number of unique items that would need to be added before a scale out occurs or (non scaling) before it rejects addition of unique items.
 9 | * EXPANSION expansion - This option will specify the bloom filter as scaling and controls the size of the sub filter that will be created upon scale out / expansion of the bloom filter.
10 | * NONSCALING - This option will configure the bloom filter as non scaling; it cannot expand / scale beyond its specified capacity.
11 |
12 | ## Examples
13 |
14 | ```
15 | 127.0.0.1:6379> BF.RESERVE key 0.01 1000
16 | OK
17 | 127.0.0.1:6379> BF.RESERVE key 0.1 1000000
18 | (error) ERR item exists
19 | ```
20 | ```
21 | 127.0.0.1:6379> BF.RESERVE bf_expansion 0.0001 5000 EXPANSION 3
22 | OK
23 | ```
24 | ```
25 | 127.0.0.1:6379> BF.RESERVE bf_nonscaling 0.0001 5000 NONSCALING
26 | OK
27 | ```
28 |


--------------------------------------------------------------------------------
/commands/bgrewriteaof.md:
--------------------------------------------------------------------------------
 1 | Instruct Valkey to start an [Append Only File][tpaof] rewrite process.
 2 | The rewrite will create a small optimized version of the current Append Only
 3 | File.
 4 |
 5 | [tpaof]: ../topics/persistence.md#append-only-file
 6 |
 7 | If `BGREWRITEAOF` fails, no data gets lost as the old AOF will be untouched.
 8 |
 9 | The rewrite will be only triggered by Valkey if there is not already a background
10 | process doing persistence.
11 |
12 | Specifically:
13 |
14 | * If a Valkey child is creating a snapshot on disk, the AOF rewrite is _scheduled_ but not started until the saving child producing the RDB file terminates. In this case the `BGREWRITEAOF` will still return a positive status reply, but with an appropriate message.  You can check if an AOF rewrite is scheduled looking at the `INFO` command.
15 | * If an AOF rewrite is already in progress the command returns an error and no
16 |   AOF rewrite will be scheduled for a later time.
17 | * If the AOF rewrite could start, but the attempt at starting it fails (for instance because of an error in creating the child process), an error is returned to the caller.
18 |
19 | The AOF rewrite is automatically triggered by Valkey, however the
20 | `BGREWRITEAOF` command can be used to trigger a rewrite at any time.
21 |
22 | Please refer to the [persistence documentation][tp] for detailed information.
23 |
24 | [tp]: ../topics/persistence.md
25 |
26 |


--------------------------------------------------------------------------------
/commands/bgsave.md:
--------------------------------------------------------------------------------
 1 | Save the DB in background.
 2 |
 3 | Normally the OK code is immediately returned.
 4 | Valkey forks, the parent continues to serve the clients, the child saves the DB
 5 | on disk then exits.
 6 |
 7 | An error is returned if there is already a background save running or if there
 8 | is another non-background-save process running, specifically an in-progress AOF
 9 | rewrite.
10 |
11 | If `BGSAVE SCHEDULE` is used, the command will immediately return `OK` when an
12 | AOF rewrite is in progress and schedule the background save to run at the next
13 | opportunity.
14 |
15 | If `BGSAVE CANCEL` is used, it will immediately terminate any in-progress RDB save or replication full sync process.
16 | In case a background save is scheduled to run (e.g. using `BGSAVE SCHEDULE` command) the scheduled execution will be
17 | cancelled as well.
18 |
19 | A client may be able to check if the operation succeeded using the `LASTSAVE`
20 | command.
21 |
22 | Please refer to the [persistence documentation][tp] for detailed information.
23 |
24 | [tp]: ../topics/persistence.md
25 |
26 |


--------------------------------------------------------------------------------
/commands/bitfield_ro.md:
--------------------------------------------------------------------------------
 1 | Read-only variant of the `BITFIELD` command.
 2 | It is like the original `BITFIELD` but only accepts `!GET` subcommand and can safely be used in read-only replicas.
 3 |
 4 | Since the original `BITFIELD` has `!SET` and `!INCRBY` options it is technically flagged as a writing command in the Valkey command table.
 5 | For this reason read-only replicas in a Valkey Cluster will redirect it to the master instance even if the connection is in read-only mode (see the `READONLY` command of Valkey Cluster).
 6 |
 7 | See original `BITFIELD` for more details.
 8 |
 9 | ```
10 | BITFIELD_RO hello GET i8 16
11 | ```
12 |


--------------------------------------------------------------------------------
/commands/blmove.md:
--------------------------------------------------------------------------------
 1 | `BLMOVE` is the blocking variant of `LMOVE`.
 2 | When `source` contains elements, this command behaves exactly like `LMOVE`.
 3 | When used inside a `MULTI`/`EXEC` block, this command behaves exactly like `LMOVE`.
 4 | When `source` is empty, Valkey will block the connection until another client
 5 | pushes to it or until `timeout` (a double value specifying the maximum number of seconds to block) is reached.
 6 | A `timeout` of zero can be used to block indefinitely.
 7 |
 8 | This command comes in place of the now deprecated `BRPOPLPUSH`. Doing
 9 | `BLMOVE RIGHT LEFT` is equivalent.
10 |
11 | See `LMOVE` for more information.
12 |
13 | ## Pattern: Reliable queue
14 |
15 | Please see the pattern description in the `LMOVE` documentation.
16 |
17 | ## Pattern: Circular list
18 |
19 | Please see the pattern description in the `LMOVE` documentation.
20 |


--------------------------------------------------------------------------------
/commands/blmpop.md:
--------------------------------------------------------------------------------
1 | `BLMPOP` is the blocking variant of `LMPOP`.
2 |
3 | When any of the lists contains elements, this command behaves exactly like `LMPOP`.
4 | When used inside a `MULTI`/`EXEC` block, this command behaves exactly like `LMPOP`.
5 | When all lists are empty, Valkey will block the connection until another client pushes to it or until the `timeout` (a double value specifying the maximum number of seconds to block) elapses.
6 | A `timeout` of zero can be used to block indefinitely.
7 |
8 | See `LMPOP` for more information.
9 |


--------------------------------------------------------------------------------
/commands/brpop.md:
--------------------------------------------------------------------------------
 1 | `BRPOP` is a blocking list pop primitive.
 2 | It is the blocking version of `RPOP` because it blocks the connection when there
 3 | are no elements to pop from any of the given lists.
 4 | An element is popped from the tail of the first list that is non-empty, with the
 5 | given keys being checked in the order that they are given.
 6 |
 7 | See the [BLPOP documentation][cb] for the exact semantics, since `BRPOP` is
 8 | identical to `BLPOP` with the only difference being that it pops elements from
 9 | the tail of a list instead of popping from the head.
10 |
11 | [cb]: blpop.md
12 |
13 | ## Examples
14 |
15 | ```
16 | 127.0.0.1:6379> DEL list1 list2
17 | (integer) 0
18 | 127.0.0.1:6379> RPUSH list1 a b c
19 | (integer) 3
20 | 127.0.0.1:6379> BRPOP list1 list2 0
21 | 1) "list1"
22 | 2) "c"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/brpoplpush.md:
--------------------------------------------------------------------------------
 1 | `BRPOPLPUSH` is the blocking variant of `RPOPLPUSH`.
 2 | When `source` contains elements, this command behaves exactly like `RPOPLPUSH`.
 3 | When used inside a `MULTI`/`EXEC` block, this command behaves exactly like `RPOPLPUSH`.
 4 | When `source` is empty, Valkey will block the connection until another client
 5 | pushes to it or until `timeout` is reached.
 6 | A `timeout` of zero can be used to block indefinitely.
 7 |
 8 | See `RPOPLPUSH` for more information.
 9 |
10 | ## Pattern: Reliable queue
11 |
12 | Please see the pattern description in the `RPOPLPUSH` documentation.
13 |
14 | ## Pattern: Circular list
15 |
16 | Please see the pattern description in the `RPOPLPUSH` documentation.
17 |


--------------------------------------------------------------------------------
/commands/bzmpop.md:
--------------------------------------------------------------------------------
1 | `BZMPOP` is the blocking variant of `ZMPOP`.
2 |
3 | When any of the sorted sets contains elements, this command behaves exactly like `ZMPOP`.
4 | When used inside a `MULTI`/`EXEC` block, this command behaves exactly like `ZMPOP`.
5 | When all sorted sets are empty, Valkey will block the connection until another client adds members to one of the keys or until the `timeout` (a double value specifying the maximum number of seconds to block) elapses.
6 | A `timeout` of zero can be used to block indefinitely.
7 |
8 | See `ZMPOP` for more information.
9 |


--------------------------------------------------------------------------------
/commands/bzpopmax.md:
--------------------------------------------------------------------------------
 1 | `BZPOPMAX` is the blocking variant of the sorted set `ZPOPMAX` primitive.
 2 |
 3 | It is the blocking version because it blocks the connection when there are no
 4 | members to pop from any of the given sorted sets.
 5 | A member with the highest score is popped from first sorted set that is
 6 | non-empty, with the given keys being checked in the order that they are given.
 7 |
 8 | The `timeout` argument is interpreted as a double value specifying the maximum
 9 | number of seconds to block. A timeout of zero can be used to block indefinitely.
10 |
11 | See the [BZPOPMIN documentation][cb] for the exact semantics, since `BZPOPMAX`
12 | is identical to `BZPOPMIN` with the only difference being that it pops members
13 | with the highest scores instead of popping the ones with the lowest scores.
14 |
15 | [cb]: bzpopmin.md
16 |
17 | ## Examples
18 |
19 | ```
20 | 127.0.0.1:6379> DEL zset1 zset2
21 | (integer) 0
22 | 127.0.0.1:6379> ZADD zset1 0 a 1 b 2 c
23 | (integer) 3
24 | 127.0.0.1:6379> BZPOPMAX zset1 zset2 0
25 | 1) "zset1"
26 | 2) "c"
27 | 3) "2"
28 | ```
29 |


--------------------------------------------------------------------------------
/commands/bzpopmin.md:
--------------------------------------------------------------------------------
 1 | `BZPOPMIN` is the blocking variant of the sorted set `ZPOPMIN` primitive.
 2 |
 3 | It is the blocking version because it blocks the connection when there are no
 4 | members to pop from any of the given sorted sets.
 5 | A member with the lowest score is popped from first sorted set that is
 6 | non-empty, with the given keys being checked in the order that they are given.
 7 |
 8 | The `timeout` argument is interpreted as a double value specifying the maximum
 9 | number of seconds to block. A timeout of zero can be used to block indefinitely.
10 |
11 | See the [BLPOP documentation][cl] for the exact semantics, since `BZPOPMIN` is
12 | identical to `BLPOP` with the only difference being the data structure being
13 | popped from.
14 |
15 | [cl]: blpop.md
16 |
17 | ## Examples
18 |
19 | ```
20 | 127.0.0.1:6379> DEL zset1 zset2
21 | (integer) 0
22 | 127.0.0.1:6379> ZADD zset1 0 a 1 b 2 c
23 | (integer) 3
24 | 127.0.0.1:6379> BZPOPMIN zset1 zset2 0
25 | 1) "zset1"
26 | 2) "a"
27 | 3) "0"
28 | ```
29 |


--------------------------------------------------------------------------------
/commands/client-caching.md:
--------------------------------------------------------------------------------
 1 | This command controls the tracking of the keys in the next command executed
 2 | by the connection, when tracking is enabled in `OPTIN` or `OPTOUT` mode.
 3 | Please check the
 4 | [client side caching documentation](../topics/client-side-caching.md) for
 5 | background information.
 6 |
 7 | When tracking is enabled Valkey, using the `CLIENT TRACKING` command, it is
 8 | possible to specify the `OPTIN` or `OPTOUT` options, so that keys
 9 | in read only commands are not automatically remembered by the server to
10 | be invalidated later. When we are in `OPTIN` mode, we can enable the
11 | tracking of the keys in the next command by calling `CLIENT CACHING yes`
12 | immediately before it. Similarly when we are in `OPTOUT` mode, and keys
13 | are normally tracked, we can avoid the keys in the next command to be
14 | tracked using `CLIENT CACHING no`.
15 |
16 | Basically the command sets a state in the connection, that is valid only
17 | for the next command execution, that will modify the behavior of client
18 | tracking.
19 |


--------------------------------------------------------------------------------
/commands/client-capa.md:
--------------------------------------------------------------------------------
 1 | Clients can declare their capabilities to Valkey using the `CLIENT CAPA` command, and Valkey
 2 | will adjust the corresponding features for the current connection based on the declared client capabilities.
 3 |
 4 | Multiple capabilities can be declared in the command. If any capabilities are unrecognized,
 5 | Valkey will ignore them instead of returning an error.
 6 |
 7 | The capabilities currently supported are:
 8 |
 9 | * `redirect` - This indicates that the client is capable of handling redirect messages.
10 |   When accessing a replica node in standalone mode, if a data operation is performed (read or write commands),
11 |   Valkey will return `-REDIRECT primary-ip:port` to this connection.
12 |   Using the `READONLY` command can enable this connection to execute read commands on the replica node.
13 |


--------------------------------------------------------------------------------
/commands/client-getname.md:
--------------------------------------------------------------------------------
1 | The `CLIENT GETNAME` returns the name of the current connection as set by `CLIENT SETNAME`. Since every new connection starts without an associated name, if no name was assigned a null bulk reply is returned.
2 |


--------------------------------------------------------------------------------
/commands/client-getredir.md:
--------------------------------------------------------------------------------
1 | This command returns the client ID we are redirecting our
2 | [tracking](../topics/client-side-caching.md) notifications to. We set a client
3 | to redirect to when using `CLIENT TRACKING` to enable tracking. However in
4 | order to avoid forcing client libraries implementations to remember the
5 | ID notifications are redirected to, this command exists in order to improve
6 | introspection and allow clients to check later if redirection is active
7 | and towards which client ID.
8 |


--------------------------------------------------------------------------------
/commands/client-help.md:
--------------------------------------------------------------------------------
1 | The `CLIENT HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/client-id.md:
--------------------------------------------------------------------------------
 1 | The command just returns the ID of the current connection. Every connection
 2 | ID has certain guarantees:
 3 |
 4 | 1. It is never repeated, so if `CLIENT ID` returns the same number, the caller can be sure that the underlying client did not disconnect and reconnect the connection, but it is still the same connection.
 5 | 2. The ID is monotonically incremental. If the ID of a connection is greater than the ID of another connection, it is guaranteed that the second connection was established with the server at a later time.
 6 |
 7 | This command is especially useful together with `CLIENT UNBLOCK`.
 8 | Check the `CLIENT UNBLOCK` command page for a pattern involving the two commands.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> CLIENT ID
14 | (integer) 2873
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/client-import-source.md:
--------------------------------------------------------------------------------
 1 | When the client sync data from a Redis-like server to Valkey using some sync tools like [RedisShake](https://github.com/tair-opensource/RedisShake), Valkey performs expiration and eviction as usual because it's a primary, which may cause data corruption. For example, the client calls `set key 1 ex 1` on the source server and this command is transferred to the destination server. Then the client calls `incr key` on the source server before the key expired, there will be a key on the source server with the value of 2. But when the command arrived at the destination server, the key may be expired and has deleted. So there will be a key on the destination server with the value of 1, which is inconsistent with the source server. Sync tools can solve this problem by setting `import-mode` config to `yes` and declaring their connections as `IMPORT-SOURCE`.
 2 |
 3 | The `CLIENT IMPORT-SOURCE` command mark this client as an import source if import-mode is enabled and can visit expired keys. The following modes are available:
 4 |
 5 | * `ON`. In this mode the client can visit expired keys.
 6 | * `OFF`. This is the default mode in which the client works as a normal client.
 7 |
 8 | ## Notes
 9 |
10 | The server needs to be configured with `import-mode yes` before marking a client connection as an import source.
11 |


--------------------------------------------------------------------------------
/commands/client-info.md:
--------------------------------------------------------------------------------
 1 | The command returns information and statistics about the current client connection in a mostly human readable format.
 2 |
 3 | The reply format is identical to that of `CLIENT LIST`, and the content consists only of information about the current client.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> CLIENT INFO
 9 | id=2875 addr=127.0.0.1:38610 laddr=127.0.0.1:6379 fd=10 name= age=0 idle=0 flags=N capa= db=0 sub=0 psub=0 ssub=0 multi=-1 watch=0 qbuf=26 qbuf-free=20448 argv-mem=10 multi-mem=0 rbs=16384 rbp=16384 obl=0 oll=0 omem=0 tot-mem=37786 events=r cmd=client|info user=default redir=-1 resp=2 lib-name= lib-ver=
10 | ```
11 |


--------------------------------------------------------------------------------
/commands/client-no-evict.md:
--------------------------------------------------------------------------------
1 | The `CLIENT NO-EVICT` command sets the [client eviction](../topics/clients.md#client-eviction) mode for the current connection.
2 |
3 | When turned on and client eviction is configured, the current connection will be excluded from the client eviction process even if we're above the configured client eviction threshold.
4 |
5 | When turned off, the current client will be re-included in the pool of potential clients to be evicted (and evicted if needed).
6 |
7 | See [client eviction](../topics/clients.md#client-eviction) for more details.
8 |


--------------------------------------------------------------------------------
/commands/client-no-touch.md:
--------------------------------------------------------------------------------
1 | The `CLIENT NO-TOUCH` command controls whether commands sent by the client will alter the LRU/LFU of the keys they access.
2 |
3 | When turned on, the current client will not change LFU/LRU stats, unless it sends the `TOUCH` command.
4 |
5 | When turned off, the client touches LFU/LRU stats just as a normal client.
6 |


--------------------------------------------------------------------------------
/commands/client-reply.md:
--------------------------------------------------------------------------------
 1 | Sometimes it can be useful for clients to completely disable replies from the Valkey server. For example when the client sends fire and forget commands or performs a mass loading of data, or in caching contexts where new data is streamed constantly. In such contexts to use server time and bandwidth in order to send back replies to clients, which are going to be ignored, is considered wasteful.
 2 |
 3 | The `CLIENT REPLY` command controls whether the server will reply the client's commands. The following modes are available:
 4 |
 5 | * `ON`. This is the default mode in which the server returns a reply to every command.
 6 | * `OFF`. In this mode the server will not reply to client commands.
 7 | * `SKIP`. This mode skips the reply of command immediately after it.
 8 |
 9 | **Note:**
10 | Starting with Valkey 9.0, the `CLIENT REPLY` command is disallowed inside a transaction `(MULTI/EXEC)`. In earlier versions, using `CLIENT REPLY` within a transaction could corrupt the reply stream. Attempting to use it within a transaction now results in an error reply.


--------------------------------------------------------------------------------
/commands/client-setinfo.md:
--------------------------------------------------------------------------------
 1 | The `CLIENT SETINFO` command assigns various info attributes to the current connection which are displayed in the output of `CLIENT LIST` and `CLIENT INFO`.
 2 |
 3 | Client libraries are expected to pipeline this command after authentication on all connections
 4 | and ignore failures since they could be connected to an older version that doesn't support them.
 5 |
 6 | Currently the supported attributes are:
 7 | * `lib-name` - meant to hold the name of the client library that's in use.
 8 | * `lib-ver` - meant to hold the client library's version.
 9 |
10 | There is no limit to the length of these attributes. However it is not possible to use spaces, newlines, or other non-printable characters that would violate the format of the `CLIENT LIST` reply.
11 |
12 | Note that these attributes are **not** cleared by the RESET command.
13 |


--------------------------------------------------------------------------------
/commands/client-setname.md:
--------------------------------------------------------------------------------
 1 | The `CLIENT SETNAME` command assigns a name to the current connection.
 2 |
 3 | The assigned name is displayed in the output of `CLIENT LIST` so that it is possible to identify the client that performed a given connection.
 4 |
 5 | For instance when Valkey is used in order to implement a queue, producers and consumers of messages may want to set the name of the connection according to their role.
 6 |
 7 | There is no limit to the length of the name that can be assigned if not the usual limits of the String type (512 MB). However it is not possible to use spaces in the connection name as this would violate the format of the `CLIENT LIST` reply.
 8 |
 9 | It is possible to entirely remove the connection name setting it to the empty string, that is not a valid connection name since it serves to this specific purpose.
10 |
11 | The connection name can be inspected using `CLIENT GETNAME`.
12 |
13 | Every new connection starts without an assigned name.
14 |
15 | Tip: setting names to connections is a good way to debug connection leaks due to bugs in the application using Valkey.
16 |


--------------------------------------------------------------------------------
/commands/client-trackinginfo.md:
--------------------------------------------------------------------------------
 1 | The command returns information about the current client connection's use of the [server assisted client side caching](../topics/client-side-caching.md) feature.
 2 |
 3 | Here's the list of tracking information sections and their respective values:
 4 |
 5 | * **flags**: A list of tracking flags used by the connection. The flags and their meanings are as follows:
 6 |   * `off`: The connection isn't using server assisted client side caching.
 7 |   * `on`: Server assisted client side caching is enabled for the connection.
 8 |   * `bcast`: The client uses broadcasting mode.
 9 |   * `optin`: The client does not cache keys by default.
10 |   * `optout`: The client caches keys by default.
11 |   * `caching-yes`: The next command will cache keys (exists only together with `optin`).
12 |   * `caching-no`: The next command won't cache keys (exists only together with `optout`).
13 |   * `noloop`: The client isn't notified about keys modified by itself.
14 |   * `broken_redirect`: The client ID used for redirection isn't valid anymore.
15 | * **redirect**: The client ID used for notifications redirection, or -1 when none.
16 | * **prefixes**: A list of key prefixes for which notifications are sent to the client.
17 |


--------------------------------------------------------------------------------
/commands/client-unpause.md:
--------------------------------------------------------------------------------
1 | `CLIENT UNPAUSE` is used to resume command processing for all clients that were paused by `CLIENT PAUSE`.
2 |


--------------------------------------------------------------------------------
/commands/client.md:
--------------------------------------------------------------------------------
1 | This is a container command for client connection commands.
2 |
3 | To see the list of available commands you can call `CLIENT HELP`.


--------------------------------------------------------------------------------
/commands/cluster-addslotsrange.md:
--------------------------------------------------------------------------------
 1 | The `CLUSTER ADDSLOTSRANGE` is similar to the `CLUSTER ADDSLOTS` command in that they both assign hash slots to nodes.
 2 |
 3 | The difference between the two commands is that `CLUSTER ADDSLOTS` takes a list of slots to assign to the node, while `CLUSTER ADDSLOTSRANGE` takes a list of slot ranges (specified by start and end slots) to assign to the node.
 4 |
 5 | ## Example
 6 |
 7 | To assign slots 1 2 3 4 5 to the node, the `CLUSTER ADDSLOTS` command is:
 8 |
 9 |     > CLUSTER ADDSLOTS 1 2 3 4 5
10 |     OK
11 |
12 | The same operation can be completed with the following `CLUSTER ADDSLOTSRANGE` command:
13 |
14 |     > CLUSTER ADDSLOTSRANGE 1 5
15 |     OK
16 |
17 |
18 | ## Usage in Valkey Cluster
19 |
20 | This command only works in cluster mode and is useful in the following Valkey Cluster operations:
21 |
22 | 1. To create a new cluster, `CLUSTER ADDSLOTSRANGE` is used to initially set up primary nodes splitting the available hash slots among them.
23 | 2. In order to fix a broken cluster where certain slots are unassigned.
24 |


--------------------------------------------------------------------------------
/commands/cluster-bumpepoch.md:
--------------------------------------------------------------------------------
1 | Advances the cluster config epoch.
2 |
3 | The `CLUSTER BUMPEPOCH` command triggers an increment to the cluster's config epoch from the connected node. The epoch will be incremented if the node's config epoch is zero, or if it is less than the cluster's greatest epoch.
4 |
5 | **Note:** config epoch management is performed internally by the cluster, and relies on obtaining a consensus of nodes. The `CLUSTER BUMPEPOCH` attempts to increment the config epoch **WITHOUT** getting the consensus, so using it may violate the "last failover wins" rule. Use it with caution.
6 |


--------------------------------------------------------------------------------
/commands/cluster-countkeysinslot.md:
--------------------------------------------------------------------------------
 1 | Returns the number of keys in the specified Valkey Cluster hash slot. The
 2 | command only queries the local data set, so contacting a node
 3 | that is not serving the specified hash slot will always result in a count of
 4 | zero being returned.
 5 |
 6 | ```
 7 | > CLUSTER COUNTKEYSINSLOT 7000
 8 | (integer) 50341
 9 | ```
10 |


--------------------------------------------------------------------------------
/commands/cluster-delslotsrange.md:
--------------------------------------------------------------------------------
 1 | The `CLUSTER DELSLOTSRANGE` command is similar to the `CLUSTER DELSLOTS` command in that they both remove hash slots from the node.
 2 | The difference is that `CLUSTER DELSLOTS` takes a list of hash slots to remove from the node, while `CLUSTER DELSLOTSRANGE` takes a list of slot ranges (specified by start and end slots) to remove from the node.
 3 |
 4 | ## Example
 5 |
 6 | To remove slots 1 2 3 4 5 from the node, the `CLUSTER DELSLOTS` command is:
 7 |
 8 |     > CLUSTER DELSLOTS 1 2 3 4 5
 9 |     OK
10 |
11 | The same operation can be completed with the following `CLUSTER DELSLOTSRANGE` command:
12 |
13 |     > CLUSTER DELSLOTSRANGE 1 5
14 |     OK
15 |
16 | However, note that:
17 |
18 | 1. The command only works if all the specified slots are already associated with the node.
19 | 2. The command fails if the same slot is specified multiple times.
20 | 3. As a side effect of the command execution, the node may go into *down* state because not all hash slots are covered.
21 |
22 | ## Usage in Valkey Cluster
23 |
24 | This command only works in cluster mode and may be useful for
25 | debugging and in order to manually orchestrate a cluster configuration
26 | when a new cluster is created. It is currently not used by `valkey-cli`,
27 | and mainly exists for API completeness.
28 |


--------------------------------------------------------------------------------
/commands/cluster-flushslots.md:
--------------------------------------------------------------------------------
1 | Deletes all slots from a node.
2 |
3 | The `CLUSTER FLUSHSLOTS` deletes all information about slots from the connected node. It can only be called when the database is empty.
4 |


--------------------------------------------------------------------------------
/commands/cluster-getkeysinslot.md:
--------------------------------------------------------------------------------
 1 | The command returns an array of keys names stored in the contacted node and
 2 | hashing to the specified hash slot. The maximum number of keys to return
 3 | is specified via the `count` argument, so that it is possible for the user
 4 | of this API to batch-processing keys.
 5 |
 6 | The main usage of this command is during rehashing of cluster slots from one
 7 | node to another. The way the rehashing is performed is exposed in the Valkey
 8 | Cluster specification, or in a more simple to digest form, as an appendix
 9 | of the `CLUSTER SETSLOT` command documentation.
10 |
11 | ```
12 | > CLUSTER GETKEYSINSLOT 7000 3
13 | 1) "key_39015"
14 | 2) "key_89793"
15 | 3) "key_92937"
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/cluster-help.md:
--------------------------------------------------------------------------------
1 | The `CLUSTER HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/cluster-keyslot.md:
--------------------------------------------------------------------------------
 1 | Returns an integer identifying the hash slot the specified key hashes to.
 2 | This command is mainly useful for debugging and testing, since it exposes
 3 | via an API the underlying Valkey implementation of the hashing algorithm.
 4 | Example use cases for this command:
 5 |
 6 | 1. Client libraries may use Valkey in order to test their own hashing algorithm, generating random keys and hashing them with both their local implementation and using Valkey `CLUSTER KEYSLOT` command, then checking if the result is the same.
 7 | 2. Humans may use this command in order to check what is the hash slot, and then the associated Valkey Cluster node, responsible for a given key.
 8 |
 9 | ## Example
10 |
11 | ```
12 | > CLUSTER KEYSLOT somekey
13 | (integer) 11058
14 | > CLUSTER KEYSLOT foo{hash_tag}
15 | (integer) 2515
16 | > CLUSTER KEYSLOT bar{hash_tag}
17 | (integer) 2515
18 | ```
19 |
20 | Note that the command implements the full hashing algorithm, including support for **hash tags**, that is the special property of Valkey Cluster key hashing algorithm, of hashing just what is between `{` and `}` if such a pattern is found inside the key name, in order to force multiple keys to be handled by the same node.
21 |


--------------------------------------------------------------------------------
/commands/cluster-myid.md:
--------------------------------------------------------------------------------
1 | Returns the node's id.
2 |
3 | The `CLUSTER MYID` command returns the unique, auto-generated identifier that is associated with the connected cluster node.
4 |


--------------------------------------------------------------------------------
/commands/cluster-myshardid.md:
--------------------------------------------------------------------------------
1 | Returns the node's shard id.
2 |
3 | The `CLUSTER MYSHARDID` command returns the unique, auto-generated identifier that is associated with the shard to which the connected cluster node belongs.
4 |


--------------------------------------------------------------------------------
/commands/cluster-replicas.md:
--------------------------------------------------------------------------------
 1 | The command provides a list of replica nodes replicating from the specified
 2 | primary node. The list is provided in the same format used by `CLUSTER NODES` (please refer to its documentation for the specification of the format).
 3 |
 4 | The command will fail if the specified node is not known or if it is not
 5 | a primary according to the node table of the node receiving the command.
 6 |
 7 | Note that if a replica is added, moved, or removed from a given primary node,
 8 | and we ask `CLUSTER REPLICAS` to a node that has not yet received the
 9 | configuration update, it may show stale information. However eventually
10 | (in a matter of seconds if there are no network partitions) all the nodes
11 | will agree about the set of nodes associated with a given primary.
12 |


--------------------------------------------------------------------------------
/commands/cluster-replicate.md:
--------------------------------------------------------------------------------
 1 | The command reconfigures a node as a replica of the specified primary.
 2 | If the node receiving the command is an *empty primary*, as a side effect
 3 | of the command, the node role is changed from primary to replica.
 4 |
 5 | Once a node is turned into the replica of another primary node, there is no need
 6 | to inform the other cluster nodes about the change: heartbeat packets exchanged
 7 | between nodes will propagate the new configuration automatically.
 8 |
 9 | A replica will always accept the command, assuming that:
10 |
11 | 1. The specified node ID exists in its nodes table.
12 | 2. The specified node ID does not identify the instance we are sending the command to.
13 | 3. The specified node ID is a primary.
14 |
15 | If the node receiving the command is not already a replica, but is a primary,
16 | the command will only succeed, and the node will be converted into a replica,
17 | only if the following additional conditions are met:
18 |
19 | 1. The node is not serving any hash slots.
20 | 2. The node is empty, no keys are stored at all in the key space.
21 |
22 | If the command succeeds the new replica will immediately try to contact its primary in order to replicate from it.
23 |


--------------------------------------------------------------------------------
/commands/cluster-reset.md:
--------------------------------------------------------------------------------
 1 | Reset a Valkey Cluster node, in a more or less drastic way depending on the
 2 | reset type, that can be **hard** or **soft**. Note that this command
 3 | **does not work for primaries if they hold one or more keys**, in that case
 4 | to completely reset a primary node keys must be removed first, e.g. by using `FLUSHALL` first,
 5 | and then `CLUSTER RESET`.
 6 |
 7 | Effects on the node:
 8 |
 9 | 1. All the other nodes in the cluster are forgotten.
10 | 2. All the assigned / open slots are reset, so the slots-to-nodes mapping is totally cleared.
11 | 3. If the node is a replica it is turned into an (empty) primary. Its dataset is flushed, so at the end the node will be an empty primary.
12 | 4. **Hard reset only**: a new Node ID is generated.
13 | 5. **Hard reset only**: `currentEpoch` and `configEpoch` vars are set to 0.
14 | 6. The new configuration is persisted on disk in the node cluster configuration file.
15 |
16 | This command is mainly useful to re-provision a Valkey Cluster node
17 | in order to be used in the context of a new, different cluster. The command
18 | is also extensively used by the Valkey Cluster testing framework in order to
19 | reset the state of the cluster every time a new test unit is executed.
20 |
21 | If no reset type is specified, the default is **soft**.
22 |


--------------------------------------------------------------------------------
/commands/cluster-saveconfig.md:
--------------------------------------------------------------------------------
 1 | Forces a node to save the `nodes.conf` configuration on disk. Before to return
 2 | the command calls `fsync(2)` in order to make sure the configuration is
 3 | flushed on the computer disk.
 4 |
 5 | This command is mainly used in the event a `nodes.conf` node state file
 6 | gets lost / deleted for some reason, and we want to generate it again from
 7 | scratch. It can also be useful in case of mundane alterations of a node cluster
 8 | configuration via the `CLUSTER` command in order to ensure the new configuration
 9 | is persisted on disk, however all the commands should normally be able to
10 | auto schedule to persist the configuration on disk when it is important
11 | to do so for the correctness of the system in the event of a restart.
12 |


--------------------------------------------------------------------------------
/commands/cluster-set-config-epoch.md:
--------------------------------------------------------------------------------
 1 | This command sets a specific *config epoch* in a fresh node. It only works when:
 2 |
 3 | 1. The nodes table of the node is empty.
 4 | 2. The node current *config epoch* is zero.
 5 |
 6 | These prerequisites are needed since usually, manually altering the
 7 | configuration epoch of a node is unsafe, we want to be sure that the node with
 8 | the higher configuration epoch value (that is the last that failed over) wins
 9 | over other nodes in claiming the hash slots ownership.
10 |
11 | However there is an exception to this rule, and it is when a new
12 | cluster is created from scratch. Valkey Cluster *config epoch collision
13 | resolution* algorithm can deal with new nodes all configured with the
14 | same configuration at startup, but this process is slow and should be
15 | the exception, only to make sure that whatever happens, two more
16 | nodes eventually always move away from the state of having the same
17 | configuration epoch.
18 |
19 | So, using `CLUSTER SET-CONFIG-EPOCH`, when a new cluster is created, we can
20 | assign a different progressive configuration epoch to each node before
21 | joining the cluster together.
22 |


--------------------------------------------------------------------------------
/commands/cluster-slaves.md:
--------------------------------------------------------------------------------
 1 | **A note about the word slave used in this man page and command name**: the Valkey project no longer uses the words "master" and "slave". Please use the new command `CLUSTER REPLICAS`. The command `CLUSTER SLAVES` will continue to work for backward compatibility.
 2 |
 3 | The command provides a list of replica nodes replicating from the specified
 4 | primary node. The list is provided in the same format used by `CLUSTER NODES` (please refer to its documentation for the specification of the format).
 5 |
 6 | The command will fail if the specified node is not known or if it is not
 7 | a primary according to the node table of the node receiving the command.
 8 |
 9 | Note that if a replica is added, moved, or removed from a given primary node,
10 | and we ask `CLUSTER SLAVES` to a node that has not yet received the
11 | configuration update, it may show stale information. However eventually
12 | (in a matter of seconds if there are no network partitions) all the nodes
13 | will agree about the set of nodes associated with a given primary.
14 |


--------------------------------------------------------------------------------
/commands/cluster.md:
--------------------------------------------------------------------------------
1 | This is a container command for Valkey Cluster commands.
2 |
3 | To see the list of available commands you can call `CLUSTER HELP`.
4 |


--------------------------------------------------------------------------------
/commands/command-count.md:
--------------------------------------------------------------------------------
1 | Returns the total number of commands in this Valkey server.
2 |
3 | ## Examples
4 |
5 | ```
6 | 127.0.0.1:6379> COMMAND COUNT
7 | (integer) 241
8 | ```
9 |


--------------------------------------------------------------------------------
/commands/command-getkeys.md:
--------------------------------------------------------------------------------
 1 | Returns @array-reply of keys from a full Valkey command.
 2 |
 3 | `COMMAND GETKEYS` is a helper command to let you find the keys
 4 | from a full Valkey command.
 5 |
 6 | `COMMAND` provides information on how to find the key names of each command (see `firstkey`, [key specifications](../topics/key-specs.md#logical-operation-flags), and `movablekeys`),
 7 | but in some cases it's not possible to find keys of certain commands and then the entire command must be parsed to discover some / all key names.
 8 | You can use `COMMAND GETKEYS` or `COMMAND GETKEYSANDFLAGS` to discover key names directly from how Valkey parses the commands.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> COMMAND GETKEYS MSET a b c d e f
14 | 1) "a"
15 | 2) "c"
16 | 3) "e"
17 | 127.0.0.1:6379> COMMAND GETKEYS EVAL "not consulted" 3 key1 key2 key3 arg1 arg2 arg3 argN
18 | 1) "key1"
19 | 2) "key2"
20 | 3) "key3"
21 | 127.0.0.1:6379> COMMAND GETKEYS SORT mylist ALPHA STORE outlist
22 | 1) "mylist"
23 | 2) "outlist"
24 | ```
25 |


--------------------------------------------------------------------------------
/commands/command-getkeysandflags.md:
--------------------------------------------------------------------------------
 1 | Returns @array-reply of keys from a full Valkey command and their usage flags.
 2 |
 3 | `COMMAND GETKEYSANDFLAGS` is a helper command to let you find the keys from a full Valkey command together with flags indicating what each key is used for.
 4 |
 5 | `COMMAND` provides information on how to find the key names of each command (see `firstkey`, [key specifications](../topics/key-specs.md#logical-operation-flags), and `movablekeys`),
 6 | but in some cases it's not possible to find keys of certain commands and then the entire command must be parsed to discover some / all key names.
 7 | You can use `COMMAND GETKEYS` or `COMMAND GETKEYSANDFLAGS` to discover key names directly from how Valkey parses the commands.
 8 |
 9 | Refer to [key specifications](../topics/key-specs.md#logical-operation-flags) for information about the meaning of the key flags.
10 |
11 | ## Examples
12 |
13 | ```
14 | 127.0.0.1:6379> COMMAND GETKEYS MSET a b c d e f
15 | 1) "a"
16 | 2) "c"
17 | 3) "e"
18 | 127.0.0.1:6379> COMMAND GETKEYS EVAL "not consulted" 3 key1 key2 key3 arg1 arg2 arg3 argN
19 | 1) "key1"
20 | 2) "key2"
21 | 3) "key3"
22 | 127.0.0.1:6379> COMMAND GETKEYSANDFLAGS LMOVE mylist1 mylist2 left left
23 | 1) 1) "mylist1"
24 |    2) 1) RW
25 |       2) access
26 |       3) delete
27 | 2) 1) "mylist2"
28 |    2) 1) RW
29 |       2) insert
30 | ```
31 |


--------------------------------------------------------------------------------
/commands/command-help.md:
--------------------------------------------------------------------------------
1 | The `COMMAND HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/command-list.md:
--------------------------------------------------------------------------------
1 | Return an array of the server's command names.
2 |
3 | You can use the optional _FILTERBY_ modifier to apply one of the following filters:
4 |
5 |  - **MODULE module-name**: get the commands that belong to the module specified by _module-name_.
6 |  - **ACLCAT category**: get the commands in the [ACL category](../topics/acl.md#command-categories) specified by _category_.
7 |  - **PATTERN pattern**: get the commands that match the given glob-like _pattern_.
8 |


--------------------------------------------------------------------------------
/commands/commandlog-help.md:
--------------------------------------------------------------------------------
1 | The `COMMANDLOG HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/commandlog-len.md:
--------------------------------------------------------------------------------
 1 | The `COMMANDLOG LEN` command returns the current number of entries in the specified type of command log.
 2 |
 3 | A new entry is added to the specified command log whenever a command exceeds the corresponding threshold. There are currently three different types of command log, each with an independent threshold, including `commandlog-execution-slower-than`, `commandlog-request-larger-than`, and `commandlog-reply-larger-than`.
 4 |
 5 | The maximum number of entries in the different command log is governed by the `commandlog-slow-execution-max-len`, `commandlog-large-request-max-len` and `commandlog-large-reply-max-len` configurations.
 6 |
 7 | Once the command log reaches its maximal size, the oldest entry is removed whenever a new entry is created.
 8 |
 9 | The command log can be cleared with the `COMMANDLOG RESET` command.
10 |


--------------------------------------------------------------------------------
/commands/commandlog-reset.md:
--------------------------------------------------------------------------------
1 | This command resets the specified type of command log, clearing all entries in it.
2 |
3 | Once deleted the information is lost forever.
4 |


--------------------------------------------------------------------------------
/commands/commandlog.md:
--------------------------------------------------------------------------------
1 | This is a container command for command log management commands.
2 |
3 | To see the list of available commands you can call `COMMANDLOG HELP`.
4 |


--------------------------------------------------------------------------------
/commands/config-get.md:
--------------------------------------------------------------------------------
 1 | The `CONFIG GET` command is used to read the configuration parameters of a
 2 | running Valkey server.
 3 |
 4 | The symmetric command used to alter the configuration at run time is `CONFIG
 5 | SET`.
 6 |
 7 | `CONFIG GET` takes multiple arguments, which are glob-style patterns.
 8 | Any configuration parameter matching any of the patterns are reported as a list
 9 | of key-value pairs.
10 | Example:
11 |
12 | ```
13 | 127.0.0.1:6379> config get *max-*-entries* maxmemory
14 |  1) "maxmemory"
15 |  2) "0"
16 |  3) "hash-max-listpack-entries"
17 |  4) "512"
18 |  5) "hash-max-ziplist-entries"
19 |  6) "512"
20 |  7) "set-max-intset-entries"
21 |  8) "512"
22 |  9) "zset-max-listpack-entries"
23 | 10) "128"
24 | 11) "zset-max-ziplist-entries"
25 | 12) "128"
26 | ```
27 |
28 | You can obtain a list of all the supported configuration parameters by typing
29 | `CONFIG GET *` in an open `valkey-cli` prompt.
30 |
31 | All the supported parameters have the same meaning of the equivalent
32 | configuration parameter used in the [valkey.conf][hgcarr22rc] file:
33 |
34 | [hgcarr22rc]: http://github.com/valkey-io/valkey/raw/unstable/valkey.conf
35 |
36 | Note that you should look at the valkey.conf file relevant to the version you're
37 | working with as configuration options might change between versions. The link
38 | above is to the latest development version.
39 |


--------------------------------------------------------------------------------
/commands/config-help.md:
--------------------------------------------------------------------------------
1 | The `CONFIG HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/config-resetstat.md:
--------------------------------------------------------------------------------
 1 | Resets the statistics reported by Valkey using the `INFO` and `LATENCY HISTOGRAM` commands.
 2 |
 3 | The following is a non-exhaustive list of values that are reset:
 4 |
 5 | * Keyspace hits and misses
 6 | * Number of expired keys
 7 | * Command and error statistics
 8 | * Connections received, rejected and evicted
 9 | * Persistence statistics
10 | * Active defragmentation statistics
11 |


--------------------------------------------------------------------------------
/commands/config.md:
--------------------------------------------------------------------------------
1 | This is a container command for runtime configuration commands.
2 |
3 | To see the list of available commands you can call `CONFIG HELP`.
4 |


--------------------------------------------------------------------------------
/commands/copy.md:
--------------------------------------------------------------------------------
 1 | This command copies the value stored at the `source` key to the `destination`
 2 | key.
 3 |
 4 | By default, the `destination` key is created in the logical database used by the
 5 | connection. The `DB` option allows specifying an alternative logical database
 6 | index for the destination key.
 7 |
 8 | The command returns zero when the `destination` key already exists. The
 9 | `REPLACE` option removes the `destination` key before copying the value to it.
10 |
11 | ## Examples
12 |
13 | ```
14 | SET dolly "sheep"
15 | COPY dolly clone
16 | GET clone
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/dbsize.md:
--------------------------------------------------------------------------------
1 | Return the number of keys in the currently-selected database.
2 |


--------------------------------------------------------------------------------
/commands/debug.md:
--------------------------------------------------------------------------------
1 | The `DEBUG` command is an internal command.
2 | It is meant to be used for developing and testing Valkey.


--------------------------------------------------------------------------------
/commands/decr.md:
--------------------------------------------------------------------------------
 1 | Decrements the number stored at `key` by one.
 2 | If the key does not exist, it is set to `0` before performing the operation.
 3 | An error is returned if the key contains a value of the wrong type or contains a
 4 | string that can not be represented as integer.
 5 | This operation is limited to **64 bit signed integers**.
 6 |
 7 | See `INCR` for extra information on increment/decrement operations.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> SET mykey "10"
13 | OK
14 | 127.0.0.1:6379> DECR mykey
15 | (integer) 9
16 | 127.0.0.1:6379> SET mykey "234293482390480948029348230948"
17 | OK
18 | 127.0.0.1:6379> DECR mykey
19 | (error) ERR value is not an integer or out of range
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/decrby.md:
--------------------------------------------------------------------------------
 1 | Decrements the number stored at `key` by `decrement`.
 2 | If the key does not exist, it is set to `0` before performing the operation.
 3 | An error is returned if the key contains a value of the wrong type or contains a
 4 | string that can not be represented as integer.
 5 | This operation is limited to 64 bit signed integers.
 6 |
 7 | See `INCR` for extra information on increment/decrement operations.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> SET mykey "10"
13 | OK
14 | 127.0.0.1:6379> DECRBY mykey 3
15 | (integer) 7
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/del.md:
--------------------------------------------------------------------------------
 1 | Removes the specified keys.
 2 | A key is ignored if it does not exist.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> SET key1 "Hello"
 8 | OK
 9 | 127.0.0.1:6379> SET key2 "World"
10 | OK
11 | 127.0.0.1:6379> DEL key1 key2 key3
12 | (integer) 2
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/discard.md:
--------------------------------------------------------------------------------
1 | Flushes all previously queued commands in a [transaction][tt] and restores the
2 | connection state to normal.
3 |
4 | [tt]: ../topics/transactions.md
5 |
6 | If `WATCH` was used, `DISCARD` unwatches all keys watched by the connection.
7 |


--------------------------------------------------------------------------------
/commands/dump.md:
--------------------------------------------------------------------------------
 1 | Serialize the value stored at key in a Valkey-specific format and return it to
 2 | the user.
 3 | The returned value can be synthesized back into a Valkey key using the `RESTORE`
 4 | command.
 5 |
 6 | The serialization format is opaque and non-standard, however it has a few
 7 | semantic characteristics:
 8 |
 9 | * It contains a 64-bit checksum that is used to make sure errors will be
10 |   detected.
11 |   The `RESTORE` command makes sure to check the checksum before synthesizing a
12 |   key using the serialized value.
13 | * Values are encoded in the same format used by RDB.
14 | * An RDB version is encoded inside the serialized value, so that different Valkey
15 |   versions with incompatible RDB formats will refuse to process the serialized
16 |   value.
17 |
18 | The serialized value does NOT contain expire information.
19 | In order to capture the time to live of the current value the `PTTL` command
20 | should be used.
21 |
22 | If `key` does not exist a nil bulk reply is returned.
23 |
24 | ## Examples
25 |
26 | ```
27 | > SET mykey 10
28 | OK
29 | > DUMP mykey
30 | "\x00\xc0\n\n\x00n\x9fWE\x0e\xaec\xbb"
31 | ```
32 |


--------------------------------------------------------------------------------
/commands/echo.md:
--------------------------------------------------------------------------------
1 | Returns `message`.
2 |
3 | ## Examples
4 |
5 | ```
6 | 127.0.0.1:6379> ECHO "Hello World!"
7 | "Hello World!"
8 | ```
9 |


--------------------------------------------------------------------------------
/commands/eval_ro.md:
--------------------------------------------------------------------------------
 1 | This is a read-only variant of the `EVAL` command that cannot execute commands that modify data.
 2 |
 3 | For more information about when to use this command vs `EVAL`, please refer to [Read-only scripts](../topics/programmability.md#read-only-scripts).
 4 |
 5 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | > SET mykey "Hello"
11 | OK
12 |
13 | > EVAL_RO "return server.call('GET', KEYS[1])" 1 mykey
14 | "Hello"
15 |
16 | > EVAL_RO "return server.call('DEL', KEYS[1])" 1 mykey
17 | (error) ERR Error running script (call to b0d697da25b13e49157b2c214a4033546aba2104): @user_script:1: @user_script: 1: Write commands are not allowed from read-only scripts.
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/evalsha.md:
--------------------------------------------------------------------------------
1 | Evaluate a script from the server's cache by its SHA1 digest.
2 |
3 | The server caches scripts by using the `SCRIPT LOAD` command.
4 | The command is otherwise identical to `EVAL`.
5 |
6 | Please refer to the [Valkey Programmability](../topics/programmability.md) and [Introduction to Eval Scripts](../topics/eval-intro.md) for more information about Lua scripts.
7 |


--------------------------------------------------------------------------------
/commands/evalsha_ro.md:
--------------------------------------------------------------------------------
1 | This is a read-only variant of the `EVALSHA` command that cannot execute commands that modify data.
2 |
3 | For more information about when to use this command vs `EVALSHA`, please refer to [Read-only scripts](../topics/programmability.md#read-only-scripts).
4 |
5 | For more information about `EVALSHA` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
6 |


--------------------------------------------------------------------------------
/commands/exec.md:
--------------------------------------------------------------------------------
 1 | Executes all previously queued commands in a [transaction][tt] and restores the
 2 | connection state to normal.
 3 |
 4 | [tt]: ../topics/transactions.md
 5 |
 6 | When using `WATCH`, `EXEC` will execute commands only if the watched keys were
 7 | not modified, allowing for a [check-and-set mechanism][ttc].
 8 |
 9 | [ttc]: ../topics/transactions.md#cas
10 |


--------------------------------------------------------------------------------
/commands/exists.md:
--------------------------------------------------------------------------------
 1 | Returns if `key` exists.
 2 |
 3 | The user should be aware that if the same existing key is mentioned in the arguments multiple times, it will be counted multiple times. So if `somekey` exists, `EXISTS somekey somekey` will return 2.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> SET key1 "Hello"
 9 | OK
10 | 127.0.0.1:6379> EXISTS key1
11 | (integer) 1
12 | 127.0.0.1:6379> EXISTS nosuchkey
13 | (integer) 0
14 | 127.0.0.1:6379> SET key2 "World"
15 | OK
16 | 127.0.0.1:6379> EXISTS key1 key2 nosuchkey
17 | (integer) 2
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/expiretime.md:
--------------------------------------------------------------------------------
 1 | Returns the absolute Unix timestamp (since January 1, 1970) in seconds at which the given key will expire.
 2 |
 3 | See also the `PEXPIRETIME` command which returns the same information with milliseconds resolution.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> SET mykey "Hello"
 9 | OK
10 | 127.0.0.1:6379> EXPIREAT mykey 33177117420
11 | (integer) 1
12 | 127.0.0.1:6379> EXPIRETIME mykey
13 | (integer) 33177117420
14 | ```
15 |


--------------------------------------------------------------------------------
/commands/fcall_ro.md:
--------------------------------------------------------------------------------
1 | This is a read-only variant of the `FCALL` command that cannot execute commands that modify data.
2 |
3 | For more information about when to use this command vs `FCALL`, please refer to [Read-only scripts](../topics/programmability.md#read-only_scripts).
4 |
5 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
6 |


--------------------------------------------------------------------------------
/commands/flushall.md:
--------------------------------------------------------------------------------
 1 | Delete all the keys of all the existing databases, not just the currently selected one.
 2 | This command never fails.
 3 |
 4 | By default, `FLUSHALL` will synchronously flush all the databases.
 5 | Setting the **lazyfree-lazy-user-flush** configuration directive to "yes" changes the default flush mode to asynchronous.
 6 |
 7 | It is possible to use one of the following modifiers to dictate the flushing mode explicitly:
 8 |
 9 | * `ASYNC`: flushes the databases asynchronously
10 | * `!SYNC`: flushes the databases synchronously
11 |
12 | Note: an asynchronous `FLUSHALL` command only deletes keys that were present at the time the command was invoked. Keys created during an asynchronous flush will be unaffected.
13 |


--------------------------------------------------------------------------------
/commands/flushdb.md:
--------------------------------------------------------------------------------
 1 | Delete all the keys of the currently selected DB.
 2 | This command never fails.
 3 |
 4 | By default, `FLUSHDB` will synchronously flush all keys from the database.
 5 | Setting the **lazyfree-lazy-user-flush** configuration directive to "yes" changes the default flush mode to asynchronous.
 6 |
 7 | It is possible to use one of the following modifiers to dictate the flushing mode explicitly:
 8 |
 9 | * `ASYNC`: flushes the database asynchronously
10 | * `!SYNC`: flushes the database synchronously
11 |
12 | Note: an asynchronous `FLUSHDB` command only deletes keys that were present at the time the command was invoked. Keys created during an asynchronous flush will be unaffected.
13 |


--------------------------------------------------------------------------------
/commands/function-delete.md:
--------------------------------------------------------------------------------
 1 | Delete a library and all its functions.
 2 |
 3 | This command deletes the library called _library-name_ and all functions in it.
 4 | If the library doesn't exist, the server returns an error.
 5 |
 6 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
 7 |
 8 | ## Examples
 9 |
10 | ```
11 | 127.0.0.1:6379> FUNCTION LOAD "#!lua name=mylib \n server.register_function('myfunc', function(keys, args) return 'hello' end)"
12 | "mylib"
13 | 127.0.0.1:6379> FCALL myfunc 0
14 | "hello"
15 | 127.0.0.1:6379> FUNCTION DELETE mylib
16 | OK
17 | 127.0.0.1:6379> FCALL myfunc 0
18 | (error) ERR Function not found
19 | ```
20 |


--------------------------------------------------------------------------------
/commands/function-dump.md:
--------------------------------------------------------------------------------
 1 | Return the serialized payload of loaded libraries.
 2 | You can restore the serialized payload later with the `FUNCTION RESTORE` command.
 3 |
 4 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
 5 |
 6 | ## Examples
 7 |
 8 | The following example shows how to dump loaded libraries using `FUNCTION DUMP` and then it calls `FUNCTION FLUSH` deletes all the libraries.
 9 | Then, it restores the original libraries from the serialized payload with `FUNCTION RESTORE`.
10 |
11 | ```
12 | 127.0.0.1:6379> FUNCTION LOAD "#!lua name=mylib \n server.register_function('myfunc', function(keys, args) return args[1] end)"
13 | "mylib"
14 | 127.0.0.1:6379> FUNCTION DUMP
15 | "\xf5\xc3@X@]\x1f#!lua name=mylib \n server.registe\rr_function('my@\x0b\x02', @\x06`\x12\nkeys, args) 6\x03turn`\x0c\a[1] end)\x0c\x00\xba\x98\xc2\xa2\x13\x0e$\a"
16 | 127.0.0.1:6379> FUNCTION FLUSH
17 | OK
18 | 127.0.0.1:6379> FUNCTION RESTORE "\xf5\xc3@X@]\x1f#!lua name=mylib \n server.registe\rr_function('my@\x0b\x02', @\x06`\x12\nkeys, args) 6\x03turn`\x0c\a[1] end)\x0c\x00\xba\x98\xc2\xa2\x13\x0e$\a"
19 | OK
20 | 127.0.0.1:6379> FUNCTION LIST
21 | 1) 1) "library_name"
22 |    2) "mylib"
23 |    3) "engine"
24 |    4) "LUA"
25 |    5) "functions"
26 |    6) 1) 1) "name"
27 |          2) "myfunc"
28 |          3) "description"
29 |          4) (nil)
30 |          5) "flags"
31 |          6) (empty array)
32 | ```
33 |


--------------------------------------------------------------------------------
/commands/function-flush.md:
--------------------------------------------------------------------------------
1 | Deletes all the libraries.
2 |
3 | Unless called with the optional mode argument, the `lazyfree-lazy-user-flush` configuration directive sets the effective behavior. Valid modes are:
4 |
5 | * `ASYNC`: Asynchronously flush the libraries.
6 | * `!SYNC`: Synchronously flush the libraries.
7 |
8 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
9 |


--------------------------------------------------------------------------------
/commands/function-help.md:
--------------------------------------------------------------------------------
1 | The `FUNCTION HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/function-kill.md:
--------------------------------------------------------------------------------
1 | Kill a function that is currently executing.
2 |
3 |
4 | The `FUNCTION KILL` command can be used only on functions that did not modify the dataset during their execution (since stopping a read-only function does not violate the scripting engine's guaranteed atomicity).
5 |
6 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
7 |


--------------------------------------------------------------------------------
/commands/function-list.md:
--------------------------------------------------------------------------------
 1 | Return information about the functions and libraries.
 2 |
 3 | You can use the optional `LIBRARYNAME` argument to specify a pattern for matching library names.
 4 | The optional `WITHCODE` modifier will cause the server to include the libraries source implementation in the reply.
 5 |
 6 | The following information is provided for each of the libraries in the response:
 7 |
 8 | * **library_name:** the name of the library.
 9 | * **engine:** the engine of the library.
10 | * **functions:** the list of functions in the library.
11 |   Each function has the following fields:
12 |   * **name:** the name of the function.
13 |   * **description:** the function's description.
14 |   * **flags:** an array of [function flags](../topics/functions-intro.md#function-flags).
15 | * **library_code:** the library's source code (when given the `WITHCODE` modifier).
16 |
17 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
18 |


--------------------------------------------------------------------------------
/commands/function-restore.md:
--------------------------------------------------------------------------------
 1 | Restore libraries from the serialized payload.
 2 |
 3 | You can use the optional _policy_ argument to provide a policy for handling existing libraries.
 4 | The following policies are allowed:
 5 |
 6 | * **APPEND:** appends the restored libraries to the existing libraries and aborts on collision.
 7 |   This is the default policy.
 8 | * **FLUSH:** deletes all existing libraries before restoring the payload.
 9 | * **REPLACE:** appends the restored libraries to the existing libraries, replacing any existing ones in case of name collisions. Note that this policy doesn't prevent function name collisions, only libraries.
10 |
11 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
12 |


--------------------------------------------------------------------------------
/commands/function-stats.md:
--------------------------------------------------------------------------------
 1 | Return information about the function that's currently running and information about the available execution engines.
 2 |
 3 | The reply is map with two keys:
 4 |
 5 | 1. `running_script`: information about the running script.
 6 |   If there's no in-flight function, the server replies with a _nil_.
 7 |   Otherwise, this is a map with the following keys:
 8 |   * **name:** the name of the function.
 9 |   * **command:** the command and arguments used for invoking the function.
10 |   * **duration_ms:** the function's runtime duration in milliseconds.
11 | 2. `engines`: this is a map of maps. Each entry in the map represent a single engine.
12 |    Engine map contains statistics about the engine like number of functions and number of libraries.
13 |
14 |
15 | You can use this command to inspect the invocation of a long-running function and decide whether kill it with the `FUNCTION KILL` command.
16 |
17 | For more information please refer to [Introduction to Valkey Functions](../topics/functions-intro.md).
18 |


--------------------------------------------------------------------------------
/commands/function.md:
--------------------------------------------------------------------------------
1 | This is a container command for function commands.
2 |
3 | To see the list of available commands you can call `FUNCTION HELP`.


--------------------------------------------------------------------------------
/commands/geodist.md:
--------------------------------------------------------------------------------
 1 | Return the distance between two members in the geospatial index represented by the sorted set.
 2 |
 3 | Given a sorted set representing a geospatial index, populated using the `GEOADD` command, the command returns the distance between the two specified members in the specified unit.
 4 |
 5 | If one or both the members are missing, the command returns NULL.
 6 |
 7 | The unit must be one of the following, and defaults to meters:
 8 |
 9 | * **m** for meters.
10 | * **km** for kilometers.
11 | * **mi** for miles.
12 | * **ft** for feet.
13 |
14 | The distance is computed assuming that the Earth is a perfect sphere, so errors up to 0.5% are possible in edge cases.
15 |
16 | ## Examples
17 |
18 | ```
19 | 127.0.0.1:6379> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
20 | (integer) 2
21 | 127.0.0.1:6379> GEODIST Sicily Palermo Catania
22 | "166274.1516"
23 | 127.0.0.1:6379> GEODIST Sicily Palermo Catania km
24 | "166.2742"
25 | 127.0.0.1:6379> GEODIST Sicily Palermo Catania mi
26 | "103.3182"
27 | 127.0.0.1:6379> GEODIST Sicily Foo Bar
28 | (nil)
29 | ```
30 |


--------------------------------------------------------------------------------
/commands/geopos.md:
--------------------------------------------------------------------------------
 1 | Return the positions (longitude,latitude) of all the specified members of the geospatial index represented by the sorted set at *key*.
 2 |
 3 | Given a sorted set representing a geospatial index, populated using the `GEOADD` command, it is often useful to obtain back the coordinates of specified members. When the geospatial index is populated via `GEOADD` the coordinates are converted into a 52 bit geohash, so the coordinates returned may not be exactly the ones used in order to add the elements, but small errors may be introduced.
 4 |
 5 | The command can accept a variable number of arguments so it always returns an array of positions even when a single element is specified.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
11 | (integer) 2
12 | 127.0.0.1:6379> GEOPOS Sicily Palermo Catania NonExisting
13 | 1) 1) "13.36138933897018433"
14 |    2) "38.11555639549629859"
15 | 2) 1) "15.08726745843887329"
16 |    2) "37.50266842333162032"
17 | 3) (nil)
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/georadius_ro.md:
--------------------------------------------------------------------------------
1 | Read-only variant of the `GEORADIUS` command.
2 |
3 | This command is identical to the `GEORADIUS` command, except that it doesn't support the optional `STORE` and `STOREDIST` parameters.
4 |


--------------------------------------------------------------------------------
/commands/georadiusbymember.md:
--------------------------------------------------------------------------------
 1 | This command is exactly like `GEORADIUS` with the sole difference that instead
 2 | of taking, as the center of the area to query, a longitude and latitude value, it takes the name of a member already existing inside the geospatial index represented by the sorted set.
 3 |
 4 | The position of the specified member is used as the center of the query.
 5 |
 6 | Please check the example below and the `GEORADIUS` documentation for more information about the command and its options.
 7 |
 8 | Note that `GEORADIUSBYMEMBER_RO` was added to provide a read-only command that can be used in replicas. See the `GEORADIUS` page for more information.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> GEOADD Sicily 13.583333 37.316667 "Agrigento"
14 | (integer) 1
15 | 127.0.0.1:6379> GEOADD Sicily 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"
16 | (integer) 2
17 | 127.0.0.1:6379> GEORADIUSBYMEMBER Sicily Agrigento 100 km
18 | 1) "Agrigento"
19 | 2) "Palermo"
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/georadiusbymember_ro.md:
--------------------------------------------------------------------------------
1 | Read-only variant of the `GEORADIUSBYMEMBER` command.
2 |
3 | This command is identical to the `GEORADIUSBYMEMBER` command, except that it doesn't support the optional `STORE` and `STOREDIST` parameters.
4 |


--------------------------------------------------------------------------------
/commands/get.md:
--------------------------------------------------------------------------------
 1 | Get the value of `key`.
 2 | If the key does not exist the special value `nil` is returned.
 3 | An error is returned if the value stored at `key` is not a string, because `GET`
 4 | only handles string values.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> GET nonexisting
10 | (nil)
11 | 127.0.0.1:6379> SET mykey "Hello"
12 | OK
13 | 127.0.0.1:6379> GET mykey
14 | "Hello"
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/getbit.md:
--------------------------------------------------------------------------------
 1 | Returns the bit value at _offset_ in the string value stored at _key_.
 2 |
 3 | When _offset_ is beyond the string length, the string is assumed to be a
 4 | contiguous space with 0 bits.
 5 | When _key_ does not exist it is assumed to be an empty string, so _offset_ is
 6 | always out of range and the value is also assumed to be a contiguous space with
 7 | 0 bits.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> SETBIT mykey 7 1
13 | (integer) 0
14 | 127.0.0.1:6379> GETBIT mykey 0
15 | (integer) 0
16 | 127.0.0.1:6379> GETBIT mykey 7
17 | (integer) 1
18 | 127.0.0.1:6379> GETBIT mykey 100
19 | (integer) 0
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/getdel.md:
--------------------------------------------------------------------------------
 1 | Get the value of `key` and delete the key.
 2 | This command is similar to `GET`, except for the fact that it also deletes the key on success (if and only if the key's value type is a string).
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> SET mykey "Hello"
 8 | OK
 9 | 127.0.0.1:6379> GETDEL mykey
10 | "Hello"
11 | 127.0.0.1:6379> GET mykey
12 | (nil)
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/getex.md:
--------------------------------------------------------------------------------
 1 | Get the value of `key` and optionally set its expiration.
 2 | `GETEX` is similar to `GET`, but is a write command with additional options.
 3 |
 4 | ## Options
 5 |
 6 | The `GETEX` command supports a set of options that modify its behavior:
 7 |
 8 | * `EX` *seconds* -- Set the specified expire time, in seconds.
 9 | * `PX` *milliseconds* -- Set the specified expire time, in milliseconds.
10 | * `EXAT` *timestamp-seconds* -- Set the specified Unix time at which the key will expire, in seconds.
11 | * `PXAT` *timestamp-milliseconds* -- Set the specified Unix time at which the key will expire, in milliseconds.
12 | * `PERSIST` -- Remove the time to live associated with the key.
13 |
14 | ## Examples
15 |
16 | ```
17 | 127.0.0.1:6379> SET mykey "Hello"
18 | OK
19 | 127.0.0.1:6379> GETEX mykey
20 | "Hello"
21 | 127.0.0.1:6379> TTL mykey
22 | (integer) -1
23 | 127.0.0.1:6379> GETEX mykey EX 60
24 | "Hello"
25 | 127.0.0.1:6379> TTL mykey
26 | (integer) 60
27 | ```
28 |


--------------------------------------------------------------------------------
/commands/getrange.md:
--------------------------------------------------------------------------------
 1 | Returns the substring of the string value stored at `key`, determined by the
 2 | offsets `start` and `end` (both are inclusive).
 3 | Negative offsets can be used in order to provide an offset starting from the end
 4 | of the string.
 5 | So -1 means the last character, -2 the penultimate and so forth.
 6 |
 7 | The function handles out of range requests by limiting the resulting range to
 8 | the actual length of the string.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> SET mykey "This is a string"
14 | OK
15 | 127.0.0.1:6379> GETRANGE mykey 0 3
16 | "This"
17 | 127.0.0.1:6379> GETRANGE mykey -3 -1
18 | "ing"
19 | 127.0.0.1:6379> GETRANGE mykey 0 -1
20 | "This is a string"
21 | 127.0.0.1:6379> GETRANGE mykey 10 100
22 | "string"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/getset.md:
--------------------------------------------------------------------------------
 1 | Atomically sets `key` to `value` and returns the old value stored at `key`.
 2 | Returns an error when `key` exists but does not hold a string value.  Any
 3 | previous time to live associated with the key is discarded on successful
 4 | `SET` operation.
 5 |
 6 | ## Design pattern
 7 |
 8 | `GETSET` can be used together with `INCR` for counting with atomic reset.
 9 | For example: a process may call `INCR` against the key `mycounter` every time
10 | some event occurs, but from time to time we need to get the value of the counter
11 | and reset it to zero atomically.
12 | This can be done using `GETSET mycounter "0"`:
13 |
14 | ```
15 | 127.0.0.1:6379> INCR mycounter
16 | (integer) 1
17 | 127.0.0.1:6379> GETSET mycounter "0"
18 | "1"
19 | 127.0.0.1:6379> GET mycounter
20 | "0"
21 | ```
22 |
23 | ## Examples
24 |
25 | ```
26 | 127.0.0.1:6379> SET mykey "Hello"
27 | OK
28 | 127.0.0.1:6379> GETSET mykey "World"
29 | "Hello"
30 | 127.0.0.1:6379> GET mykey
31 | "World"
32 | ```
33 |


--------------------------------------------------------------------------------
/commands/hdel.md:
--------------------------------------------------------------------------------
 1 | Removes the specified fields from the hash stored at `key`.
 2 | Specified fields that do not exist within this hash are ignored.
 3 | If `key` does not exist, it is treated as an empty hash and this command returns
 4 | `0`.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> HSET myhash field1 "foo"
10 | (integer) 1
11 | 127.0.0.1:6379> HDEL myhash field1
12 | (integer) 1
13 | 127.0.0.1:6379> HDEL myhash field2
14 | (integer) 0
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/hexists.md:
--------------------------------------------------------------------------------
 1 | Returns if `field` is an existing field in the hash stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> HSET myhash field1 "foo"
 7 | (integer) 1
 8 | 127.0.0.1:6379> HEXISTS myhash field1
 9 | (integer) 1
10 | 127.0.0.1:6379> HEXISTS myhash field2
11 | (integer) 0
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/hget.md:
--------------------------------------------------------------------------------
 1 | Returns the value associated with `field` in the hash stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> HSET myhash field1 "foo"
 7 | (integer) 1
 8 | 127.0.0.1:6379> HGET myhash field1
 9 | "foo"
10 | 127.0.0.1:6379> HGET myhash field2
11 | (nil)
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/hgetall.md:
--------------------------------------------------------------------------------
 1 | Returns all fields and values of the hash stored at `key`.
 2 | In the returned value, every field name is followed by its value, so the length
 3 | of the reply is twice the size of the hash.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> HSET myhash field1 "Hello"
 9 | (integer) 1
10 | 127.0.0.1:6379> HSET myhash field2 "World"
11 | (integer) 1
12 | 127.0.0.1:6379> HGETALL myhash
13 | 1) "field1"
14 | 2) "Hello"
15 | 3) "field2"
16 | 4) "World"
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/hincrby.md:
--------------------------------------------------------------------------------
 1 | Increments the number stored at `field` in the hash stored at `key` by
 2 | `increment`.
 3 | If `key` does not exist, a new key holding a hash is created.
 4 | If `field` does not exist the value is set to `0` before the operation is
 5 | performed.
 6 |
 7 | The range of values supported by `HINCRBY` is limited to 64 bit signed integers.
 8 |
 9 | ## Examples
10 |
11 | Since the `increment` argument is signed, both increment and decrement
12 | operations can be performed:
13 |
14 | ```
15 | 127.0.0.1:6379> HSET myhash field 5
16 | (integer) 1
17 | 127.0.0.1:6379> HINCRBY myhash field 1
18 | (integer) 6
19 | 127.0.0.1:6379> HINCRBY myhash field -1
20 | (integer) 5
21 | 127.0.0.1:6379> HINCRBY myhash field -10
22 | (integer) -5
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/hincrbyfloat.md:
--------------------------------------------------------------------------------
 1 | Increment the specified `field` of a hash stored at `key`, and representing a
 2 | floating point number, by the specified `increment`. If the increment value
 3 | is negative, the result is to have the hash field value **decremented** instead of incremented.
 4 | If the field does not exist, it is set to `0` before performing the operation.
 5 | An error is returned if one of the following conditions occur:
 6 |
 7 | * The key contains a value of the wrong type (not a hash).
 8 | * The current field content or the specified increment are not parsable as a
 9 |   double precision floating point number.
10 |
11 | The exact behavior of this command is identical to the one of the `INCRBYFLOAT`
12 | command, please refer to the documentation of `INCRBYFLOAT` for further
13 | information.
14 |
15 | ## Examples
16 |
17 | ```
18 | 127.0.0.1:6379> HSET mykey field 10.50
19 | (integer) 1
20 | 127.0.0.1:6379> HINCRBYFLOAT mykey field 0.1
21 | "10.6"
22 | 127.0.0.1:6379> HINCRBYFLOAT mykey field -5
23 | "5.6"
24 | 127.0.0.1:6379> HSET mykey field 5.0e3
25 | (integer) 0
26 | 127.0.0.1:6379> HINCRBYFLOAT mykey field 2.0e2
27 | "5200"
28 | ```
29 |
30 | ## Implementation details
31 |
32 | The command is always propagated in the replication link and the Append Only
33 | File as a `HSET` operation, so that differences in the underlying floating point
34 | math implementation will not be sources of inconsistency.
35 |


--------------------------------------------------------------------------------
/commands/hkeys.md:
--------------------------------------------------------------------------------
 1 | Returns all field names in the hash stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> HSET myhash field1 "Hello"
 7 | (integer) 1
 8 | 127.0.0.1:6379> HSET myhash field2 "World"
 9 | (integer) 1
10 | 127.0.0.1:6379> HKEYS myhash
11 | 1) "field1"
12 | 2) "field2"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/hlen.md:
--------------------------------------------------------------------------------
 1 | Returns the number of fields contained in the hash stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> HSET myhash field1 "Hello"
 7 | (integer) 1
 8 | 127.0.0.1:6379> HSET myhash field2 "World"
 9 | (integer) 1
10 | 127.0.0.1:6379> HLEN myhash
11 | (integer) 2
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/hmget.md:
--------------------------------------------------------------------------------
 1 | Returns the values associated with the specified `fields` in the hash stored at
 2 | `key`.
 3 |
 4 | For every `field` that does not exist in the hash, a `nil` value is returned.
 5 | Because non-existing keys are treated as empty hashes, running `HMGET` against
 6 | a non-existing `key` will return a list of `nil` values.
 7 |
 8 | ```
 9 | 127.0.0.1:6379> HSET myhash field1 "Hello"
10 | (integer) 1
11 | 127.0.0.1:6379> HSET myhash field2 "World"
12 | (integer) 1
13 | 127.0.0.1:6379> HMGET myhash field1 field2 nofield
14 | 1) "Hello"
15 | 2) "World"
16 | 3) (nil)
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/hmset.md:
--------------------------------------------------------------------------------
 1 | Sets the specified fields to their respective values in the hash stored at
 2 | `key`.
 3 | This command overwrites any specified fields already existing in the hash.
 4 | If `key` does not exist, a new key holding a hash is created.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> HMSET myhash field1 "Hello" field2 "World"
10 | OK
11 | 127.0.0.1:6379> HGET myhash field1
12 | "Hello"
13 | 127.0.0.1:6379> HGET myhash field2
14 | "World"
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/hscan.md:
--------------------------------------------------------------------------------
1 | See `SCAN` for `HSCAN` documentation.
2 |


--------------------------------------------------------------------------------
/commands/hset.md:
--------------------------------------------------------------------------------
 1 | Sets the specified fields to their respective values in the hash stored at `key`.
 2 |
 3 | This command overwrites the values of specified fields that exist in the hash.
 4 | If `key` doesn't exist, a new key holding a hash is created.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> HSET myhash field1 "Hello"
10 | (integer) 1
11 | 127.0.0.1:6379> HGET myhash field1
12 | "Hello"
13 | 127.0.0.1:6379> HSET myhash field2 "Hi" field3 "World"
14 | (integer) 2
15 | 127.0.0.1:6379> HGET myhash field2
16 | "Hi"
17 | 127.0.0.1:6379> HGET myhash field3
18 | "World"
19 | 127.0.0.1:6379> HGETALL myhash
20 | 1) "field1"
21 | 2) "Hello"
22 | 3) "field2"
23 | 4) "Hi"
24 | 5) "field3"
25 | 6) "World"
26 | ```
27 |


--------------------------------------------------------------------------------
/commands/hsetnx.md:
--------------------------------------------------------------------------------
 1 | Sets `field` in the hash stored at `key` to `value`, only if `field` does not
 2 | yet exist.
 3 | If `key` does not exist, a new key holding a hash is created.
 4 | If `field` already exists, this operation has no effect.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> HSETNX myhash field "Hello"
10 | (integer) 1
11 | 127.0.0.1:6379> HSETNX myhash field "World"
12 | (integer) 0
13 | 127.0.0.1:6379> HGET myhash field
14 | "Hello"
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/hstrlen.md:
--------------------------------------------------------------------------------
 1 | Returns the string length of the value associated with `field` in the hash stored at `key`. If the `key` or the `field` do not exist, 0 is returned.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> HSET myhash f1 HelloWorld f2 99 f3 -256
 7 | (integer) 3
 8 | 127.0.0.1:6379> HSTRLEN myhash f1
 9 | (integer) 10
10 | 127.0.0.1:6379> HSTRLEN myhash f2
11 | (integer) 2
12 | 127.0.0.1:6379> HSTRLEN myhash f3
13 | (integer) 4
14 | ```
15 |


--------------------------------------------------------------------------------
/commands/hvals.md:
--------------------------------------------------------------------------------
 1 | Returns all values in the hash stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> HSET myhash field1 "Hello"
 7 | (integer) 1
 8 | 127.0.0.1:6379> HSET myhash field2 "World"
 9 | (integer) 1
10 | 127.0.0.1:6379> HVALS myhash
11 | 1) "Hello"
12 | 2) "World"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/incrby.md:
--------------------------------------------------------------------------------
 1 | Increments the number stored at `key` by `increment`.
 2 | If the key does not exist, it is set to `0` before performing the operation.
 3 | An error is returned if the key contains a value of the wrong type or contains a
 4 | string that can not be represented as integer.
 5 | This operation is limited to 64 bit signed integers.
 6 |
 7 | See `INCR` for extra information on increment/decrement operations.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> SET mykey "10"
13 | OK
14 | 127.0.0.1:6379> INCRBY mykey 5
15 | (integer) 15
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/json.arrappend.md:
--------------------------------------------------------------------------------
 1 | Append one or more values to the array values at the path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
 9 | OK
10 | 127.0.0.1:6379> JSON.ARRAPPEND  k1 $[*] '"c"'
11 | 1) (integer) 1
12 | 2) (integer) 2
13 | 3) (integer) 3
14 | 127.0.0.1:6379> JSON.GET k1
15 | "[[\"c\"],[\"a\",\"c\"],[\"a\",\"b\",\"c\"]]"
16 | ```
17 |
18 | Restricted path syntax:
19 |
20 | ```bash
21 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
22 | OK
23 | 127.0.0.1:6379> JSON.ARRAPPEND  k1 [-1] '"c"'
24 | (integer) 3
25 | 127.0.0.1:6379> JSON.GET k1
26 | "[[],[\"a\"],[\"a\",\"b\",\"c\"]]"
27 | ```
28 |


--------------------------------------------------------------------------------
/commands/json.arrindex.md:
--------------------------------------------------------------------------------
 1 | Search for the first occurrence of a scalar JSON value in the arrays at the path.
 2 |
 3 |
 4 | * Out of range errors are treated by rounding the index to the array's start and end.
 5 | * If start > end, return -1 (not found).
 6 |
 7 | ## Examples
 8 |
 9 | Enhanced path syntax:
10 |
11 | ```bash
12 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"], ["a", "b", "c"]]'
13 | OK
14 | 127.0.0.1:6379> JSON.ARRINDEX k1 $[*] '"b"'
15 | 1) (integer) -1
16 | 2) (integer) -1
17 | 3) (integer) 1
18 | 4) (integer) 1
19 | ```
20 |
21 | Restricted path syntax:
22 |
23 | ```bash
24 | 127.0.0.1:6379> JSON.SET k1 . '{"children": ["John", "Jack", "Tom", "Bob", "Mike"]}'
25 | OK
26 | 127.0.0.1:6379> JSON.ARRINDEX k1 .children '"Tom"'
27 | (integer) 2
28 | ```
29 |


--------------------------------------------------------------------------------
/commands/json.arrinsert.md:
--------------------------------------------------------------------------------
 1 | Insert one or more values into the array values at path before the index.
 2 |
 3 |
 4 | * Inserting at index 0 prepends to the array.
 5 | * A negative index values is interpreted as starting from the end.
 6 | * The index must be in the array's boundary.
 7 |
 8 | ## Examples
 9 |
10 | Enhanced path syntax:
11 |
12 | ```bash
13 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
14 | OK
15 | 127.0.0.1:6379> JSON.ARRINSERT k1 $[*] 0 '"c"'
16 | 1) (integer) 1
17 | 2) (integer) 2
18 | 3) (integer) 3
19 | 127.0.0.1:6379> JSON.GET k1
20 | "[[\"c\"],[\"c\",\"a\"],[\"c\",\"a\",\"b\"]]"
21 | ```
22 |
23 | Restricted path syntax:
24 |
25 | ```bash
26 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
27 | OK
28 | 127.0.0.1:6379> JSON.ARRINSERT k1 . 0 '"c"'
29 | (integer) 4
30 | 127.0.0.1:6379> JSON.GET k1
31 | "[\"c\",[],[\"a\"],[\"a\",\"b\"]]"
32 | ```
33 |


--------------------------------------------------------------------------------
/commands/json.arrlen.md:
--------------------------------------------------------------------------------
 1 | Get length of the array at the path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '[[], [\"a\"], [\"a\", \"b\"], [\"a\", \"b\", \"c\"]]'
 9 | (error) SYNTAXERR Failed to parse JSON string due to syntax error
10 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"], ["a", "b", "c"]]'
11 | OK
12 | 127.0.0.1:6379> JSON.ARRLEN k1 $[*]
13 | 1) (integer) 0
14 | 2) (integer) 1
15 | 3) (integer) 2
16 | 4) (integer) 3
17 |
18 | 127.0.0.1:6379> JSON.SET k2 . '[[], "a", ["a", "b"], ["a", "b", "c"], 4]'
19 | OK
20 | 127.0.0.1:6379> JSON.ARRLEN k2 $[*]
21 | 1) (integer) 0
22 | 2) (nil)
23 | 3) (integer) 2
24 | 4) (integer) 3
25 | 5) (nil)
26 | ```
27 |
28 | ```bash
29 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"], ["a", "b", "c"]]'
30 | OK
31 | 127.0.0.1:6379> JSON.ARRLEN k1 [*]
32 | (integer) 0
33 | 127.0.0.1:6379> JSON.ARRLEN k1 $[3]
34 | 1) (integer) 3
35 |
36 | 127.0.0.1:6379> JSON.SET k2 . '[[], "a", ["a", "b"], ["a", "b", "c"], 4]'
37 | OK
38 | 127.0.0.1:6379> JSON.ARRLEN k2 [*]
39 | (integer) 0
40 | 127.0.0.1:6379> JSON.ARRLEN k2 $[1]
41 | 1) (nil)
42 | 127.0.0.1:6379> JSON.ARRLEN k2 $[2]
43 | 1) (integer) 2
44 | ```
45 |


--------------------------------------------------------------------------------
/commands/json.arrpop.md:
--------------------------------------------------------------------------------
 1 | Remove and return element at the index from the array. Popping an empty array returns null.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
 9 | OK
10 | 127.0.0.1:6379> JSON.ARRPOP k1 $[*]
11 | 1) (nil)
12 | 2) "\"a\""
13 | 3) "\"b\""
14 | 127.0.0.1:6379> JSON.GET k1
15 | "[[],[],[\"a\"]]"
16 | ```
17 |
18 | Restricted path syntax:
19 |
20 | ```bash
21 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"]]'
22 | OK
23 | 127.0.0.1:6379> JSON.ARRPOP k1
24 | "[\"a\",\"b\"]"
25 | 127.0.0.1:6379> JSON.GET k1
26 | "[[],[\"a\"]]"
27 |
28 | 127.0.0.1:6379> JSON.SET k2 . '[[], ["a"], ["a", "b"]]'
29 | OK
30 | 127.0.0.1:6379> JSON.ARRPOP k2 . 0
31 | "[]"
32 | 127.0.0.1:6379> JSON.GET k2
33 | "[[\"a\"],[\"a\",\"b\"]]"
34 | ```
35 |


--------------------------------------------------------------------------------
/commands/json.arrtrim.md:
--------------------------------------------------------------------------------
 1 | Trim arrays at the path so that it becomes subarray [start, end], both inclusive.
 2 |
 3 |
 4 | * If the array is empty, do nothing, return 0.
 5 | * If start < 0, treat it as 0.
 6 | * If end >= size (size of the array), treat it as size-1.
 7 | * If start >= size or start > end, empty the array and return 0.
 8 |
 9 | ## Examples
10 |
11 | Enhanced path syntax:
12 |
13 | ```bash
14 | 127.0.0.1:6379> JSON.SET k1 . '[[], ["a"], ["a", "b"], ["a", "b", "c"]]'
15 | OK
16 | 127.0.0.1:6379> JSON.ARRTRIM k1 $[*] 0 1
17 | 1) (integer) 0
18 | 2) (integer) 1
19 | 3) (integer) 2
20 | 4) (integer) 2
21 |    127.0.0.1:6379> JSON.GET k1
22 |    "[[],[\"a\"],[\"a\",\"b\"],[\"a\",\"b\"]]"
23 | ```
24 |
25 | Restricted path syntax:
26 |
27 | ```bash
28 | 127.0.0.1:6379> JSON.SET k1 . '{"children": ["John", "Jack", "Tom", "Bob", "Mike"]}'
29 | OK
30 | 127.0.0.1:6379> JSON.ARRTRIM k1 .children 0 1
31 | (integer) 2
32 | 127.0.0.1:6379> JSON.GET k1 .children
33 | "[\"John\",\"Jack\"]"
34 | ```
35 |


--------------------------------------------------------------------------------
/commands/json.clear.md:
--------------------------------------------------------------------------------
 1 | Clear the arrays or objects at the path.
 2 |
 3 | ## Examples
 4 |
 5 | ```bash
 6 | 127.0.0.1:6379> JSON.SET k1 . '[[], [0], [0,1], [0,1,2], 1, true, null, "d"]'
 7 | OK
 8 | 127.0.0.1:6379>  JSON.CLEAR k1  $[*]
 9 | (integer) 6
10 | 127.0.0.1:6379> JSON.CLEAR k1  $[*]
11 | (integer) 0
12 | 127.0.0.1:6379> JSON.SET k2 . '{"children": ["John", "Jack", "Tom", "Bob", "Mike"]}'
13 | OK
14 | 127.0.0.1:6379> JSON.CLEAR k2 .children
15 | (integer) 1
16 | 127.0.0.1:6379> JSON.GET k2 .children
17 | "[]"
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/json.del.md:
--------------------------------------------------------------------------------
 1 | Delete the JSON values at the path in a document key. If the path is the root path, it is equivalent to deleting the key from Valkey.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '{"a":{}, "b":{"a":1}, "c":{"a":1, "b":2}, "d":{"a":1, "b":2, "c":3}, "e": [1,2,3,4,5]}'
 9 | OK
10 | 127.0.0.1:6379> JSON.DEL k1 $.d.*
11 | (integer) 3
12 | 127.0.0.1:6379> JSON.GET k1
13 | "{\"a\":{},\"b\":{\"a\":1},\"c\":{\"a\":1,\"b\":2},\"d\":{},\"e\":[1,2,3,4,5]}"
14 | 127.0.0.1:6379> JSON.DEL k1 $.e[*]
15 | (integer) 5
16 | 127.0.0.1:6379> JSON.GET k1
17 | "{\"a\":{},\"b\":{\"a\":1},\"c\":{\"a\":1,\"b\":2},\"d\":{},\"e\":[]}"
18 | ```
19 |
20 | Restricted path syntax:
21 |
22 | ```bash
23 | 127.0.0.1:6379> JSON.SET k1 . '{"a":{}, "b":{"a":1}, "c":{"a":1, "b":2}, "d":{"a":1, "b":2, "c":3}, "e": [1,2,3,4,5]}'
24 | OK
25 | 127.0.0.1:6379> JSON.DEL k1 .d.*
26 | (integer) 3
27 | 127.0.0.1:6379> JSON.GET k1
28 | "{\"a\":{},\"b\":{\"a\":1},\"c\":{\"a\":1,\"b\":2},\"d\":{},\"e\":[1,2,3,4,5]}"
29 | 127.0.0.1:6379> JSON.DEL k1 .e[*]
30 | (integer) 5
31 | 127.0.0.1:6379> JSON.GET k1
32 | "{\"a\":{},\"b\":{\"a\":1},\"c\":{\"a\":1,\"b\":2},\"d\":{},\"e\":[]}"
33 | ```
34 |
35 |


--------------------------------------------------------------------------------
/commands/json.forget.md:
--------------------------------------------------------------------------------
1 | An alias of JSON.DEL


--------------------------------------------------------------------------------
/commands/json.mget.md:
--------------------------------------------------------------------------------
 1 | Get serialized JSON objects from multiple document keys at the specified path. Return null for non-existent keys or JSON paths.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '{"address":{"street":"21 2nd Street","city":"New York","state":"NY","zipcode":"10021"}}'
 9 | OK
10 | 127.0.0.1:6379> JSON.SET k2 . '{"address":{"street":"5 main Street","city":"Boston","state":"MA","zipcode":"02101"}}'
11 | OK
12 | 127.0.0.1:6379> JSON.SET k3 . '{"address":{"street":"100 Park Ave","city":"Seattle","state":"WA","zipcode":"98102"}}'
13 | OK
14 | 127.0.0.1:6379> JSON.MGET k1 k2 k3 $.address.city
15 | 1) "[\"New York\"]"
16 | 2) "[\"Boston\"]"
17 | 3) "[\"Seattle\"]"
18 | ```
19 |
20 | Restricted path syntax:
21 |
22 | ```bash
23 | 127.0.0.1:6379> JSON.SET k1 . '{"address":{"street":"21 2nd Street","city":"New York","state":"NY","zipcode":"10021"}}'
24 | OK
25 | 127.0.0.1:6379> JSON.SET k2 . '{"address":{"street":"5 main Street","city":"Boston","state":"MA","zipcode":"02101"}}'
26 | OK
27 | 127.0.0.1:6379> JSON.SET k3 . '{"address":{"street":"100 Park Ave","city":"Seattle","state":"WA","zipcode":"98102"}}'
28 | OK
29 |
30 | 127.0.0.1:6379> JSON.MGET k1 k2 k3 .address.city
31 | 1) "\"New York\""
32 | 2) "\"Seattle\""
33 | 3) "\"Seattle\""
34 | ```
35 |


--------------------------------------------------------------------------------
/commands/json.objkeys.md:
--------------------------------------------------------------------------------
 1 | Get key names in the object values at the path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 $ '{"a":{}, "b":{"a":"a"}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":{"a":3,"b":4}}, "e":1}'
 9 | OK
10 | 127.0.0.1:6379> JSON.OBJKEYS k1 $.*
11 | 1) (empty array)
12 | 2) 1) "a"
13 | 3) 1) "a"
14 |    2) "b"
15 | 4) 1) "a"
16 |    2) "b"
17 |    3) "c"
18 | 5) (empty array)
19 | 127.0.0.1:6379> JSON.OBJKEYS k1 $.d
20 | 1) 1) "a"
21 |    2) "b"
22 |    3) "c"
23 | ```
24 |
25 | Restricted path syntax:
26 |
27 | ```bash
28 | 127.0.0.1:6379> JSON.SET k1 $ '{"a":{}, "b":{"a":"a"}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":{"a":3,"b":4}}, "e":1}'
29 | OK
30 | 127.0.0.1:6379> JSON.OBJKEYS k1 .*
31 | 1) "a"
32 | 127.0.0.1:6379> JSON.OBJKEYS k1 .d
33 | 1) "a"
34 | 2) "b"
35 | 3) "c"
36 | ```
37 |


--------------------------------------------------------------------------------
/commands/json.strappend.md:
--------------------------------------------------------------------------------
 1 | Append a string to the JSON strings at the path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 $ '{"a":{"a":"a"}, "b":{"a":"a", "b":1}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":3}}'
 9 | OK
10 | 127.0.0.1:6379> JSON.STRAPPEND k1 $.a.a '"a"'
11 | 1) (integer) 2
12 | 127.0.0.1:6379> JSON.STRAPPEND k1 $.a.* '"a"'
13 | 1) (integer) 3
14 | 127.0.0.1:6379> JSON.STRAPPEND k1 $.b.* '"a"'
15 | 1) (integer) 2
16 | 2) (nil)
17 | 127.0.0.1:6379> JSON.STRAPPEND k1 $.c.* '"a"'
18 | 1) (integer) 2
19 | 2) (integer) 3
20 | 127.0.0.1:6379> JSON.STRAPPEND k1 $.c.b '"a"'
21 | 1) (integer) 4
22 | 127.0.0.1:6379> JSON.STRAPPEND k1 $.d.* '"a"'
23 | 1) (nil)
24 | 2) (integer) 2
25 | 3) (nil)
26 | ````
27 |
28 | Restricted path syntax:
29 |
30 | ```bash
31 | 127.0.0.1:6379> JSON.SET k1 . '{"a":{"a":"a"}, "b":{"a":"a", "b":1}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":3}}'
32 | OK
33 | 127.0.0.1:6379> JSON.STRAPPEND k1 .a.a '"a"'
34 | (integer) 2
35 | 127.0.0.1:6379> JSON.STRAPPEND k1 .a.* '"a"'
36 | (integer) 3
37 | 127.0.0.1:6379> JSON.STRAPPEND k1 .b.* '"a"'
38 | (integer) 2
39 | 127.0.0.1:6379> JSON.STRAPPEND k1 .c.* '"a"'
40 | (integer) 3
41 | 127.0.0.1:6379> JSON.STRAPPEND k1 .c.b '"a"'
42 | (integer) 4
43 | 127.0.0.1:6379> JSON.STRAPPEND k1 .d.* '"a"'
44 | (integer) 2
45 | ```
46 |


--------------------------------------------------------------------------------
/commands/json.strlen.md:
--------------------------------------------------------------------------------
 1 | Get lengths of the JSON string values at the path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 $ '{"a":{"a":"a"}, "b":{"a":"a", "b":1}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":3}}'
 9 | OK
10 | 127.0.0.1:6379> JSON.STRLEN k1 $.a.a
11 | 1) (integer) 1
12 | 127.0.0.1:6379> JSON.STRLEN k1 $.a.*
13 | 1) (integer) 1
14 | 127.0.0.1:6379> JSON.STRLEN k1 $.c.*
15 | 1) (integer) 1
16 | 2) (integer) 2
17 | 127.0.0.1:6379> JSON.STRLEN k1 $.c.b
18 | 1) (integer) 2
19 | 127.0.0.1:6379> JSON.STRLEN k1 $.d.*
20 | 1) (nil)
21 | 2) (integer) 1
22 | 3) (nil)
23 | ```
24 |
25 | Restricted path syntax:
26 |
27 | ```bash
28 | 127.0.0.1:6379> JSON.SET k1 $ '{"a":{"a":"a"}, "b":{"a":"a", "b":1}, "c":{"a":"a", "b":"bb"}, "d":{"a":1, "b":"b", "c":3}}'
29 | OK
30 | 127.0.0.1:6379> JSON.STRLEN k1 .a.a
31 | (integer) 1
32 | 127.0.0.1:6379> JSON.STRLEN k1 .a.*
33 | (integer) 1
34 | 127.0.0.1:6379> JSON.STRLEN k1 .c.*
35 | (integer) 1
36 | 127.0.0.1:6379> JSON.STRLEN k1 .c.b
37 | (integer) 2
38 | 127.0.0.1:6379> JSON.STRLEN k1 .d.*
39 | (integer) 1
40 | ```
41 |


--------------------------------------------------------------------------------
/commands/json.toggle.md:
--------------------------------------------------------------------------------
 1 | Toggle boolean values between true and false at the path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '{"a":true, "b":false, "c":1, "d":null, "e":"foo", "f":[], "g":{}}'
 9 | OK
10 | 127.0.0.1:6379> JSON.TOGGLE k1 $.*
11 | 1) (integer) 0
12 | 2) (integer) 1
13 | 3) (nil)
14 | 4) (nil)
15 | 5) (nil)
16 | 6) (nil)
17 | 7) (nil)
18 | 127.0.0.1:6379> JSON.TOGGLE k1 $.*
19 | 1) (integer) 1
20 | 2) (integer) 0
21 | 3) (nil)
22 | 4) (nil)
23 | 5) (nil)
24 | 6) (nil)
25 | 7) (nil)
26 | ```
27 |
28 | Restricted path syntax:
29 |
30 | ```bash
31 | 127.0.0.1:6379> JSON.SET k1 . true
32 | OK
33 | 127.0.0.1:6379> JSON.TOGGLE k1
34 | "false"
35 | 127.0.0.1:6379> JSON.TOGGLE k1
36 | "true"
37 |
38 | 127.0.0.1:6379> JSON.SET k2 . '{"isAvailable": false}'
39 | OK
40 | 127.0.0.1:6379> JSON.TOGGLE k2 .isAvailable
41 | "true"
42 | 127.0.0.1:6379> JSON.TOGGLE k2 .isAvailable
43 | "false"
44 | ```
45 |


--------------------------------------------------------------------------------
/commands/json.type.md:
--------------------------------------------------------------------------------
 1 | Report type of the values at the given path.
 2 |
 3 | ## Examples
 4 |
 5 | Enhanced path syntax:
 6 |
 7 | ```bash
 8 | 127.0.0.1:6379> JSON.SET k1 . '[1, 2.3, "foo", true, null, {}, []]'
 9 | OK
10 | 127.0.0.1:6379> JSON.TYPE k1 $[*]
11 | 1) integer
12 | 2) number
13 | 3) string
14 | 4) boolean
15 | 5) null
16 | 6) object
17 | 7) array
18 | ```
19 |
20 | Restricted path syntax:
21 |
22 | ```bash
23 | 127.0.0.1:6379> JSON.SET k1 . '{"firstName":"John","lastName":"Smith","age":27,"weight":135.25,"isAlive":true,"address":{"street":"21 2nd Street","city":"New York","state":"NY","zipcode":"10021-3100"},"phoneNumbers":[{"type":"home","number":"212 555-1234"},{"type":"office","number":"646 555-4567"}],"children":[],"spouse":null}'
24 | OK
25 | 127.0.0.1:6379> JSON.TYPE k1
26 | object
27 | 127.0.0.1:6379> JSON.TYPE k1 .children
28 | array
29 | 127.0.0.1:6379> JSON.TYPE k1 .firstName
30 | string
31 | 127.0.0.1:6379> JSON.TYPE k1 .age
32 | integer
33 | 127.0.0.1:6379> JSON.TYPE k1 .weight
34 | number
35 | 127.0.0.1:6379> JSON.TYPE k1 .isAlive
36 | boolean
37 | 127.0.0.1:6379> JSON.TYPE k1 .spouse
38 | null
39 | ```
40 |


--------------------------------------------------------------------------------
/commands/lastsave.md:
--------------------------------------------------------------------------------
1 | Return the UNIX TIME of the last DB save executed with success.
2 | A client may check if a `BGSAVE` command succeeded reading the `LASTSAVE` value,
3 | then issuing a `BGSAVE` command and checking at regular intervals every N
4 | seconds if `LASTSAVE` changed. Valkey considers the database saved successfully at startup.
5 |


--------------------------------------------------------------------------------
/commands/latency-help.md:
--------------------------------------------------------------------------------
1 | The `LATENCY HELP` command returns a helpful text describing the different
2 | subcommands.
3 |
4 | For more information refer to the [Latency Monitoring Framework page][lm].
5 |
6 | [lm]: ../topics/latency-monitor.md
7 |


--------------------------------------------------------------------------------
/commands/latency-histogram.md:
--------------------------------------------------------------------------------
 1 | `LATENCY HISTOGRAM` returns a cumulative distribution of commands' latencies in histogram format.
 2 |
 3 | By default, all available latency histograms are returned.
 4 | You can filter the reply by providing specific command names.
 5 |
 6 | Each histogram consists of the following fields:
 7 |
 8 | * Command name
 9 | * The total calls for that command
10 | * A map of time buckets:
11 |   * Each bucket represents a latency range
12 |   * Each bucket covers twice the previous bucket's range
13 |   * Empty buckets are excluded from the reply
14 |   * The tracked latencies are between 1 microsecond and roughly 1 second
15 |   * Everything above 1 second is considered +Inf
16 |   * At max, there will be log2(1,000,000,000)=30 buckets
17 |
18 | This command requires the extended latency monitoring feature to be enabled, which is the default.
19 | If you need to enable it, call `CONFIG SET latency-tracking yes`.
20 |
21 | To delete the latency histograms' data use the `CONFIG RESETSTAT` command.
22 |
23 | ## Examples
24 |
25 | ```
26 | 127.0.0.1:6379> LATENCY HISTOGRAM set
27 | 1# "set" =>
28 |    1# "calls" => (integer) 100000
29 |    2# "histogram_usec" =>
30 |       1# (integer) 1 => (integer) 99583
31 |       2# (integer) 2 => (integer) 99852
32 |       3# (integer) 4 => (integer) 99914
33 |       4# (integer) 8 => (integer) 99940
34 |       5# (integer) 16 => (integer) 99968
35 |       6# (integer) 33 => (integer) 100000
36 | ```
37 |


--------------------------------------------------------------------------------
/commands/latency-history.md:
--------------------------------------------------------------------------------
 1 | The `LATENCY HISTORY` command returns the raw data of the `event`'s latency spikes time series.
 2 |
 3 | This is useful to an application that wants to fetch raw data in order to perform monitoring, display graphs, and so forth.
 4 |
 5 | The command will return up to 160 timestamp-latency pairs for the `event`.
 6 |
 7 | Valid values for `event` are:
 8 | * `active-defrag-cycle`
 9 | * `aof-fsync-always`
10 | * `aof-stat`
11 | * `aof-rewrite-diff-write`
12 | * `aof-rename`
13 | * `aof-write`
14 | * `aof-write-active-child`
15 | * `aof-write-alone`
16 | * `aof-write-pending-fsync`
17 | * `command`
18 | * `expire-cycle`
19 | * `eviction-cycle`
20 | * `eviction-del`
21 | * `fast-command`
22 | * `fork`
23 | * `rdb-unlink-temp-file`
24 |
25 | ## Examples
26 |
27 | ```
28 | 127.0.0.1:6379> latency history command
29 | 1) 1) (integer) 1405067822
30 |    2) (integer) 251
31 | 2) 1) (integer) 1405067941
32 |    2) (integer) 1001
33 | ```
34 |
35 | For more information refer to the [Latency Monitoring Framework page][lm].
36 |
37 | [lm]: ../topics/latency-monitor.md
38 |


--------------------------------------------------------------------------------
/commands/latency-latest.md:
--------------------------------------------------------------------------------
 1 | The `LATENCY LATEST` command reports the latest latency events logged.
 2 |
 3 | Each reported event has the following fields:
 4 |
 5 | * Event name.
 6 | * Unix timestamp of the latest latency spike for the event.
 7 | * Latest event latency in millisecond.
 8 | * All-time maximum latency for this event.
 9 | * Sum of the latencies recorded in the time series for this event, added in 8.1.
10 | * The number of latency spikes recorded in the time series for this event, added in 8.1.
11 |
12 | "All-time" means the maximum latency since the Valkey instance was
13 | started, or the time that events were reset `LATENCY RESET`.
14 |
15 | ## Examples
16 |
17 | ```
18 | 127.0.0.1:6379> debug sleep 1
19 | OK
20 | (1.00s)
21 | 127.0.0.1:6379> debug sleep .25
22 | OK
23 | 127.0.0.1:6379> latency latest
24 | 1) 1) "command"
25 |    2) (integer) 1738651470
26 |    3) (integer) 254
27 |    4) (integer) 1005
28 |    5) (integer) 1259
29 |    6) (integer) 2
30 | ```
31 |
32 | For more information refer to the [Latency Monitoring Framework page][lm].
33 |
34 | [lm]: ../topics/latency-monitor.md
35 |


--------------------------------------------------------------------------------
/commands/latency-reset.md:
--------------------------------------------------------------------------------
 1 | The `LATENCY RESET` command resets the latency spikes time series of all, or only some, events.
 2 |
 3 | When the command is called without arguments, it resets all the
 4 | events, discarding the currently logged latency spike events, and resetting
 5 | the maximum event time register.
 6 |
 7 | It is possible to reset only specific events by providing the `event` names
 8 | as arguments.
 9 |
10 | Valid values for `event` are:
11 | * `active-defrag-cycle`
12 | * `aof-fsync-always`
13 | * `aof-stat`
14 | * `aof-rewrite-diff-write`
15 | * `aof-rename`
16 | * `aof-write`
17 | * `aof-write-active-child`
18 | * `aof-write-alone`
19 | * `aof-write-pending-fsync`
20 | * `command`
21 | * `expire-cycle`
22 | * `eviction-cycle`
23 | * `eviction-del`
24 | * `fast-command`
25 | * `fork`
26 | * `rdb-unlink-temp-file`
27 |
28 | For more information refer to the [Latency Monitoring Framework page][lm].
29 |
30 | [lm]: ../topics/latency-monitor.md
31 |


--------------------------------------------------------------------------------
/commands/latency.md:
--------------------------------------------------------------------------------
1 | This is a container command for latency diagnostics commands.
2 |
3 | To see the list of available commands you can call `LATENCY HELP`.


--------------------------------------------------------------------------------
/commands/lindex.md:
--------------------------------------------------------------------------------
 1 | Returns the element at index `index` in the list stored at `key`.
 2 | The index is zero-based, so `0` means the first element, `1` the second element
 3 | and so on.
 4 | Negative indices can be used to designate elements starting at the tail of the
 5 | list.
 6 | Here, `-1` means the last element, `-2` means the penultimate and so forth.
 7 |
 8 | When the value at `key` is not a list, an error is returned.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> LPUSH mylist "World"
14 | (integer) 1
15 | 127.0.0.1:6379> LPUSH mylist "Hello"
16 | (integer) 2
17 | 127.0.0.1:6379> LINDEX mylist 0
18 | "Hello"
19 | 127.0.0.1:6379> LINDEX mylist -1
20 | "World"
21 | 127.0.0.1:6379> LINDEX mylist 3
22 | (nil)
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/linsert.md:
--------------------------------------------------------------------------------
 1 | Inserts `element` in the list stored at `key` either before or after the reference
 2 | value `pivot`.
 3 |
 4 | When `key` does not exist, it is considered an empty list and no operation is
 5 | performed.
 6 |
 7 | An error is returned when `key` exists but does not hold a list value.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> RPUSH mylist "Hello"
13 | (integer) 1
14 | 127.0.0.1:6379> RPUSH mylist "World"
15 | (integer) 2
16 | 127.0.0.1:6379> LINSERT mylist BEFORE "World" "There"
17 | (integer) 3
18 | 127.0.0.1:6379> LRANGE mylist 0 -1
19 | 1) "Hello"
20 | 2) "There"
21 | 3) "World"
22 | ```
23 |


--------------------------------------------------------------------------------
/commands/llen.md:
--------------------------------------------------------------------------------
 1 | Returns the length of the list stored at `key`.
 2 | If `key` does not exist, it is interpreted as an empty list and `0` is returned.
 3 | An error is returned when the value stored at `key` is not a list.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> LPUSH mylist "World"
 9 | (integer) 1
10 | 127.0.0.1:6379> LPUSH mylist "Hello"
11 | (integer) 2
12 | 127.0.0.1:6379> LLEN mylist
13 | (integer) 2
14 | ```
15 |


--------------------------------------------------------------------------------
/commands/lpop.md:
--------------------------------------------------------------------------------
 1 | Removes and returns the first elements of the list stored at `key`.
 2 |
 3 | By default, the command pops a single element from the beginning of the list.
 4 | When provided with the optional `count` argument, the reply will consist of up
 5 | to `count` elements, depending on the list's length.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> RPUSH mylist "one" "two" "three" "four" "five"
11 | (integer) 5
12 | 127.0.0.1:6379> LPOP mylist
13 | "one"
14 | 127.0.0.1:6379> LPOP mylist 2
15 | 1) "two"
16 | 2) "three"
17 | 127.0.0.1:6379> LRANGE mylist 0 -1
18 | 1) "four"
19 | 2) "five"
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/lpush.md:
--------------------------------------------------------------------------------
 1 | Insert all the specified values at the head of the list stored at `key`.
 2 | If `key` does not exist, it is created as empty list before performing the push
 3 | operations.
 4 | When `key` holds a value that is not a list, an error is returned.
 5 |
 6 | It is possible to push multiple elements using a single command call just
 7 | specifying multiple arguments at the end of the command.
 8 | Elements are inserted one after the other to the head of the list, from the
 9 | leftmost element to the rightmost element.
10 | So for instance the command `LPUSH mylist a b c` will result into a list
11 | containing `c` as first element, `b` as second element and `a` as third element.
12 |
13 | ## Examples
14 |
15 | ```
16 | 127.0.0.1:6379> LPUSH mylist "world"
17 | (integer) 1
18 | 127.0.0.1:6379> LPUSH mylist "hello"
19 | (integer) 2
20 | 127.0.0.1:6379> LRANGE mylist 0 -1
21 | 1) "hello"
22 | 2) "world"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/lpushx.md:
--------------------------------------------------------------------------------
 1 | Inserts specified values at the head of the list stored at `key`, only if `key`
 2 | already exists and holds a list.
 3 | In contrary to `LPUSH`, no operation will be performed when `key` does not yet
 4 | exist.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> LPUSH mylist "World"
10 | (integer) 1
11 | 127.0.0.1:6379> LPUSHX mylist "Hello"
12 | (integer) 2
13 | 127.0.0.1:6379> LPUSHX myotherlist "Hello"
14 | (integer) 0
15 | 127.0.0.1:6379> LRANGE mylist 0 -1
16 | 1) "Hello"
17 | 2) "World"
18 | 127.0.0.1:6379> LRANGE myotherlist 0 -1
19 | (empty array)
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/lrem.md:
--------------------------------------------------------------------------------
 1 | Removes the first `count` occurrences of elements equal to `element` from the list
 2 | stored at `key`.
 3 | The `count` argument influences the operation in the following ways:
 4 |
 5 | * `count > 0`: Remove elements equal to `element` moving from head to tail.
 6 | * `count < 0`: Remove elements equal to `element` moving from tail to head.
 7 | * `count = 0`: Remove all elements equal to `element`.
 8 |
 9 | For example, `LREM list -2 "hello"` will remove the last two occurrences of
10 | `"hello"` in the list stored at `list`.
11 |
12 | Note that non-existing keys are treated like empty lists, so when `key` does not
13 | exist, the command will always return `0`.
14 |
15 | ## Examples
16 |
17 | ```
18 | 127.0.0.1:6379> RPUSH mylist "hello"
19 | (integer) 1
20 | 127.0.0.1:6379> RPUSH mylist "hello"
21 | (integer) 2
22 | 127.0.0.1:6379> RPUSH mylist "foo"
23 | (integer) 3
24 | 127.0.0.1:6379> RPUSH mylist "hello"
25 | (integer) 4
26 | 127.0.0.1:6379> LREM mylist -2 "hello"
27 | (integer) 2
28 | 127.0.0.1:6379> LRANGE mylist 0 -1
29 | 1) "hello"
30 | 2) "foo"
31 | ```
32 |


--------------------------------------------------------------------------------
/commands/lset.md:
--------------------------------------------------------------------------------
 1 | Sets the list element at `index` to `element`.
 2 | For more information on the `index` argument, see `LINDEX`.
 3 |
 4 | An error is returned for out of range indexes.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> RPUSH mylist "one"
10 | (integer) 1
11 | 127.0.0.1:6379> RPUSH mylist "two"
12 | (integer) 2
13 | 127.0.0.1:6379> RPUSH mylist "three"
14 | (integer) 3
15 | 127.0.0.1:6379> LSET mylist 0 "four"
16 | OK
17 | 127.0.0.1:6379> LSET mylist -2 "five"
18 | OK
19 | 127.0.0.1:6379> LRANGE mylist 0 -1
20 | 1) "four"
21 | 2) "five"
22 | 3) "three"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/memory-doctor.md:
--------------------------------------------------------------------------------
1 | The `MEMORY DOCTOR` command reports about different memory-related issues that
2 | the Valkey server experiences, and advises about possible remedies.
3 |


--------------------------------------------------------------------------------
/commands/memory-help.md:
--------------------------------------------------------------------------------
1 | The `MEMORY HELP` command returns a helpful text describing the different
2 | subcommands.
3 |


--------------------------------------------------------------------------------
/commands/memory-malloc-stats.md:
--------------------------------------------------------------------------------
1 | The `MEMORY MALLOC-STATS` command provides an internal statistics report from
2 | the memory allocator.
3 |
4 | This command is currently implemented only when using **jemalloc** as an
5 | allocator, and evaluates to a benign NOOP for all others.
6 |


--------------------------------------------------------------------------------
/commands/memory-purge.md:
--------------------------------------------------------------------------------
1 | The `MEMORY PURGE` command attempts to purge dirty pages so these can be
2 | reclaimed by the allocator.
3 |
4 | This command is currently implemented only when using **jemalloc** as an
5 | allocator, and evaluates to a benign NOOP for all others.
6 |


--------------------------------------------------------------------------------
/commands/memory-usage.md:
--------------------------------------------------------------------------------
 1 | The `MEMORY USAGE` command reports the number of bytes that a key and its value
 2 | require to be stored in RAM.
 3 |
 4 | The reported usage is the total of memory allocations for data and
 5 | administrative overheads that a key and its value require.
 6 |
 7 | For nested data types, the optional `SAMPLES` option can be provided, where
 8 | `count` is the number of sampled nested values. The samples are averaged to estimate the total size.
 9 | By default, this option is set to `5`. To sample the all of the nested values, use `SAMPLES 0`.
10 |
11 | ## Examples
12 |
13 | With Valkey v7.2.4 64-bit and **jemalloc**, the empty string measures as follows:
14 |
15 | ```
16 | > SET "" ""
17 | OK
18 | > MEMORY USAGE ""
19 | (integer) 56
20 | ```
21 |
22 | These bytes are pure overhead at the moment as no actual data is stored, and are
23 | used for maintaining the internal data structures of the server (include internal allocator fragmentation). Longer keys and
24 | values show asymptotically linear usage.
25 |
26 | ```
27 | > SET foo bar
28 | OK
29 | > MEMORY USAGE foo
30 | (integer) 56
31 | > SET foo2 mybar
32 | OK
33 | > MEMORY USAGE foo2
34 | (integer) 64
35 | > SET foo3 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
36 | OK
37 | > MEMORY USAGE foo3
38 | (integer) 160
39 | ```
40 |


--------------------------------------------------------------------------------
/commands/memory.md:
--------------------------------------------------------------------------------
1 | This is a container command for memory introspection and management commands.
2 |
3 | To see the list of available commands you can call `MEMORY HELP`.
4 |


--------------------------------------------------------------------------------
/commands/mget.md:
--------------------------------------------------------------------------------
 1 | Returns the values of all specified keys.
 2 | For every key that does not hold a string value or does not exist, the special
 3 | value `nil` is returned.
 4 | Because of this, the operation never fails.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> SET key1 "Hello"
10 | OK
11 | 127.0.0.1:6379> SET key2 "World"
12 | OK
13 | 127.0.0.1:6379> MGET key1 key2 nonexisting
14 | 1) "Hello"
15 | 2) "World"
16 | 3) (nil)
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/module-help.md:
--------------------------------------------------------------------------------
1 | The `MODULE HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/module-list.md:
--------------------------------------------------------------------------------
1 | Returns information about the modules loaded to the server.
2 |


--------------------------------------------------------------------------------
/commands/module-load.md:
--------------------------------------------------------------------------------
 1 | Loads a module from a dynamic library at runtime.
 2 |
 3 | This command loads and initializes the Valkey module from the dynamic library
 4 | specified by the `path` argument. The `path` should be the absolute path of the
 5 | library, including the full filename. Any additional arguments are passed
 6 | unmodified to the module.
 7 |
 8 | **Note**: modules can also be loaded at server startup with `loadmodule`
 9 | configuration directive in `valkey.conf`.
10 |


--------------------------------------------------------------------------------
/commands/module-loadex.md:
--------------------------------------------------------------------------------
 1 | Loads a module from a dynamic library at runtime with configuration directives.
 2 |
 3 | This is an extended version of the `MODULE LOAD` command.
 4 |
 5 | It loads and initializes the Valkey module from the dynamic library specified by the `path` argument. The `path` should be the absolute path of the library, including the full filename.
 6 |
 7 | You can use the optional `!CONFIG` argument to provide the module with configuration directives.
 8 | Any additional arguments that follow the `ARGS` keyword are passed unmodified to the module.
 9 |
10 | **Note**: modules can also be loaded at server startup with `loadmodule`
11 | configuration directive in `valkey.conf`.
12 |


--------------------------------------------------------------------------------
/commands/module-unload.md:
--------------------------------------------------------------------------------
 1 | Unloads a module.
 2 |
 3 | This command unloads the module specified by `name`. Note that the module's name
 4 | is reported by the `MODULE LIST` command, and may differ from the dynamic
 5 | library's filename.
 6 |
 7 | Known limitations:
 8 |
 9 | *   Modules that register custom data types can not be unloaded.
10 |


--------------------------------------------------------------------------------
/commands/module.md:
--------------------------------------------------------------------------------
1 | This is a container command for module management commands.
2 |
3 | To see the list of available commands you can call `MODULE HELP`.
4 |


--------------------------------------------------------------------------------
/commands/move.md:
--------------------------------------------------------------------------------
1 | Move `key` from the currently selected database (see `SELECT`) to the specified
2 | destination database.
3 | When `key` already exists in the destination database, or it does not exist in
4 | the source database, it does nothing.
5 | It is possible to use `MOVE` as a locking primitive because of this.
6 |


--------------------------------------------------------------------------------
/commands/mset.md:
--------------------------------------------------------------------------------
 1 | Sets the given keys to their respective values.
 2 | `MSET` replaces existing values with new values, just as regular `SET`.
 3 | See `MSETNX` if you don't want to overwrite existing values.
 4 |
 5 | `MSET` is atomic, so all given keys are set at once.
 6 | It is not possible for clients to see that some of the keys were updated while
 7 | others are unchanged.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> MSET key1 "Hello" key2 "World"
13 | OK
14 | 127.0.0.1:6379> GET key1
15 | "Hello"
16 | 127.0.0.1:6379> GET key2
17 | "World"
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/msetnx.md:
--------------------------------------------------------------------------------
 1 | Sets the given keys to their respective values.
 2 | `MSETNX` will not perform any operation at all even if just a single key already
 3 | exists.
 4 |
 5 | Because of this semantic `MSETNX` can be used in order to set different keys
 6 | representing different fields of a unique logic object in a way that ensures
 7 | that either all the fields or none at all are set.
 8 |
 9 | `MSETNX` is atomic, so all given keys are set at once.
10 | It is not possible for clients to see that some of the keys were updated while
11 | others are unchanged.
12 |
13 | ## Examples
14 |
15 | ```
16 | 127.0.0.1:6379> MSETNX key1 "Hello" key2 "there"
17 | (integer) 1
18 | 127.0.0.1:6379> MSETNX key2 "new" key3 "world"
19 | (integer) 0
20 | 127.0.0.1:6379> MGET key1 key2 key3
21 | 1) "Hello"
22 | 2) "there"
23 | 3) (nil)
24 | ```
25 |


--------------------------------------------------------------------------------
/commands/multi.md:
--------------------------------------------------------------------------------
1 | Marks the start of a [transaction][tt] block.
2 | Subsequent commands will be queued for atomic execution using `EXEC`.
3 |
4 | [tt]: ../topics/transactions.md
5 |


--------------------------------------------------------------------------------
/commands/object-freq.md:
--------------------------------------------------------------------------------
1 | This command returns the logarithmic access frequency counter of a Valkey object stored at `<key>`.
2 |
3 | The command is only available when the `maxmemory-policy` configuration directive is set to one of the LFU policies.
4 |


--------------------------------------------------------------------------------
/commands/object-help.md:
--------------------------------------------------------------------------------
1 | The `OBJECT HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/object-idletime.md:
--------------------------------------------------------------------------------
1 | This command returns the time in seconds since the last access to the value stored at `<key>`.
2 |
3 | The command is only available when the `maxmemory-policy` configuration directive is not set to one of the LFU policies.
4 |


--------------------------------------------------------------------------------
/commands/object-refcount.md:
--------------------------------------------------------------------------------
1 | This command returns the reference count of the stored at `<key>`.
2 |


--------------------------------------------------------------------------------
/commands/object.md:
--------------------------------------------------------------------------------
1 | This is a container command for object introspection commands.
2 |
3 | To see the list of available commands you can call `OBJECT HELP`.
4 |


--------------------------------------------------------------------------------
/commands/persist.md:
--------------------------------------------------------------------------------
 1 | Remove the existing timeout on `key`, turning the key from _volatile_ (a key
 2 | with an expire set) to _persistent_ (a key that will never expire as no timeout
 3 | is associated).
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> SET mykey "Hello"
 9 | OK
10 | 127.0.0.1:6379> EXPIRE mykey 10
11 | (integer) 1
12 | 127.0.0.1:6379> TTL mykey
13 | (integer) 10
14 | 127.0.0.1:6379> PERSIST mykey
15 | (integer) 1
16 | 127.0.0.1:6379> TTL mykey
17 | (integer) -1
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/pexpire.md:
--------------------------------------------------------------------------------
 1 | This command works exactly like `EXPIRE` but the time to live of the key is
 2 | specified in milliseconds instead of seconds.
 3 |
 4 | ## Options
 5 |
 6 | The `PEXPIRE` command supports a set of options
 7 |
 8 | * `NX` -- Set expiry only when the key has no expiry
 9 | * `XX` -- Set expiry only when the key has an existing expiry
10 | * `GT` -- Set expiry only when the new expiry is greater than current one
11 | * `LT` -- Set expiry only when the new expiry is less than current one
12 |
13 | A non-volatile key is treated as an infinite TTL for the purpose of `GT` and `LT`.
14 | The `GT`, `LT` and `NX` options are mutually exclusive.
15 |
16 | ## Examples
17 |
18 | ```
19 | 127.0.0.1:6379> SET mykey "Hello"
20 | OK
21 | 127.0.0.1:6379> PEXPIRE mykey 1500
22 | (integer) 1
23 | 127.0.0.1:6379> TTL mykey
24 | (integer) 1
25 | 127.0.0.1:6379> PTTL mykey
26 | (integer) 1480
27 | 127.0.0.1:6379> PEXPIRE mykey 1000 XX
28 | (integer) 1
29 | 127.0.0.1:6379> TTL mykey
30 | (integer) 1
31 | 127.0.0.1:6379> PEXPIRE mykey 1000 NX
32 | (integer) 0
33 | 127.0.0.1:6379> TTL mykey
34 | (integer) 1
35 | ```
36 |


--------------------------------------------------------------------------------
/commands/pexpireat.md:
--------------------------------------------------------------------------------
 1 | `PEXPIREAT` has the same effect and semantic as `EXPIREAT`, but the Unix time at
 2 | which the key will expire is specified in milliseconds instead of seconds.
 3 |
 4 | ## Options
 5 |
 6 | The `PEXPIREAT` command supports a set of options since Redis OSS 7.0:
 7 |
 8 | * `NX` -- Set expiry only when the key has no expiry
 9 | * `XX` -- Set expiry only when the key has an existing expiry
10 | * `GT` -- Set expiry only when the new expiry is greater than current one
11 | * `LT` -- Set expiry only when the new expiry is less than current one
12 |
13 | A non-volatile key is treated as an infinite TTL for the purpose of `GT` and `LT`.
14 | The `GT`, `LT` and `NX` options are mutually exclusive.
15 |
16 | ## Examples
17 |
18 | ```
19 | 127.0.0.1:6379> SET mykey "Hello"
20 | OK
21 | 127.0.0.1:6379> PEXPIREAT mykey 1555555555005
22 | (integer) 1
23 | 127.0.0.1:6379> TTL mykey
24 | (integer) -2
25 | 127.0.0.1:6379> PTTL mykey
26 | (integer) -2
27 | ```
28 |


--------------------------------------------------------------------------------
/commands/pexpiretime.md:
--------------------------------------------------------------------------------
 1 | `PEXPIRETIME` has the same semantic as `EXPIRETIME`, but returns the absolute Unix expiration timestamp in milliseconds instead of seconds.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> SET mykey "Hello"
 7 | OK
 8 | 127.0.0.1:6379> PEXPIREAT mykey 33177117420000
 9 | (integer) 1
10 | 127.0.0.1:6379> PEXPIRETIME mykey
11 | (integer) 33177117420000
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/pfadd.md:
--------------------------------------------------------------------------------
 1 | Adds all the element arguments to the HyperLogLog data structure stored at the variable name specified as first argument.
 2 |
 3 | As a side effect of this command the HyperLogLog internals may be updated to reflect a different estimation of the number of unique items added so far (the cardinality of the set).
 4 |
 5 | If the approximated cardinality estimated by the HyperLogLog changed after executing the command, `PFADD` returns 1, otherwise 0 is returned. The command automatically creates an empty HyperLogLog structure (that is, a String of a specified length and with a given encoding) if the specified key does not exist.
 6 |
 7 | To call the command without elements but just the variable name is valid, this will result into no operation performed if the variable already exists, or just the creation of the data structure if the key does not exist (in the latter case 1 is returned).
 8 |
 9 | For an introduction to HyperLogLog data structure check the `PFCOUNT` command page.
10 |
11 | ## Examples
12 |
13 | ```
14 | 127.0.0.1:6379> PFADD hll a b c d e f g
15 | (integer) 1
16 | 127.0.0.1:6379> PFCOUNT hll
17 | (integer) 7
18 | ```
19 |


--------------------------------------------------------------------------------
/commands/pfdebug.md:
--------------------------------------------------------------------------------
1 | The `PFDEBUG` command is an internal command.
2 | It is meant to be used for developing and testing Valkey.


--------------------------------------------------------------------------------
/commands/pfmerge.md:
--------------------------------------------------------------------------------
 1 | Merge multiple HyperLogLog values into a unique value that will approximate
 2 | the cardinality of the union of the observed Sets of the source HyperLogLog
 3 | structures.
 4 |
 5 | The computed merged HyperLogLog is set to the destination variable, which is
 6 | created if does not exist (defaulting to an empty HyperLogLog).
 7 |
 8 | If the destination variable exists, it is treated as one of the source sets
 9 | and its cardinality will be included in the cardinality of the computed
10 | HyperLogLog.
11 |
12 | ## Examples
13 |
14 | ```
15 | 127.0.0.1:6379> PFADD hll1 foo bar zap a
16 | (integer) 1
17 | 127.0.0.1:6379> PFADD hll2 a b c foo
18 | (integer) 1
19 | 127.0.0.1:6379> PFMERGE hll3 hll1 hll2
20 | OK
21 | 127.0.0.1:6379> PFCOUNT hll3
22 | (integer) 6
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/pfselftest.md:
--------------------------------------------------------------------------------
1 | The `PFSELFTEST` command is an internal command.
2 | It is meant to be used for developing and testing Valkey.


--------------------------------------------------------------------------------
/commands/ping.md:
--------------------------------------------------------------------------------
 1 | Returns `PONG` if no argument is provided, otherwise return a copy of the
 2 | argument as a bulk.
 3 | This command is useful for:
 4 | 1. Testing whether a connection is still alive.
 5 | 1. Verifying the server's ability to serve data - an error is returned when this isn't the case (e.g., during load from persistence or accessing a stale replica).
 6 | 1. Measuring latency.
 7 |
 8 | If the client is in RESP2 and is subscribed to a channel or a pattern, it will instead return a
 9 | multi-bulk with a "pong" in the first position and an empty bulk in the second
10 | position, unless an argument is provided in which case it returns a copy
11 | of the argument.
12 |
13 | ## Examples
14 |
15 | ```
16 | 127.0.0.1:6379> PING
17 | PONG
18 | 127.0.0.1:6379>
19 | 127.0.0.1:6379> PING "hello world"
20 | "hello world"
21 | ```
22 |


--------------------------------------------------------------------------------
/commands/psetex.md:
--------------------------------------------------------------------------------
 1 | `PSETEX` works exactly like `SETEX` with the sole difference that the expire
 2 | time is specified in milliseconds instead of seconds.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> PSETEX mykey 1000 "Hello"
 8 | OK
 9 | 127.0.0.1:6379> PTTL mykey
10 | (integer) 990
11 | 127.0.0.1:6379> GET mykey
12 | "Hello"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/psubscribe.md:
--------------------------------------------------------------------------------
 1 | Subscribes the client to the given patterns.
 2 |
 3 | Supported glob-style patterns:
 4 |
 5 | * `h?llo` subscribes to `hello`, `hallo` and `hxllo`
 6 | * `h*llo` subscribes to `hllo` and `heeeello`
 7 | * `h[ae]llo` subscribes to `hello` and `hallo,` but not `hillo`
 8 |
 9 | Use `\` to escape special characters if you want to match them verbatim.
10 |
11 | Once the client enters the subscribed state it is not supposed to issue any other commands, except for additional `SUBSCRIBE`, `SSUBSCRIBE`, `PSUBSCRIBE`, `UNSUBSCRIBE`, `SUNSUBSCRIBE`, `PUNSUBSCRIBE`, `PING`, `RESET` and `QUIT` commands.
12 | However, if RESP3 is used (see `HELLO`) it is possible for a client to issue any commands while in subscribed state.
13 |
14 | Note that `RESET` can be called to exit subscribed state.
15 |
16 | For more information, see [Pub/sub](../topics/pubsub.md).
17 |
18 |


--------------------------------------------------------------------------------
/commands/psync.md:
--------------------------------------------------------------------------------
 1 | Initiates a replication stream from the primary.
 2 |
 3 | The `PSYNC` command is called by Valkey replicas for initiating a replication
 4 | stream from the primary.
 5 |
 6 | For more information about replication in Valkey please check the
 7 | [replication page][tr].
 8 |
 9 | [tr]: ../topics/replication.md
10 |


--------------------------------------------------------------------------------
/commands/pttl.md:
--------------------------------------------------------------------------------
 1 | Like `TTL` this command returns the remaining time to live of a key that has an
 2 | expire set, with the sole difference that `TTL` returns the amount of remaining
 3 | time in seconds while `PTTL` returns it in milliseconds.
 4 |
 5 | The command returns the following values in case of errors:
 6 |
 7 | * The command returns `-2` if the key does not exist.
 8 | * The command returns `-1` if the key exists but has no associated expire.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> SET mykey "Hello"
14 | OK
15 | 127.0.0.1:6379> EXPIRE mykey 1
16 | (integer) 1
17 | 127.0.0.1:6379> PTTL mykey
18 | (integer) 989
19 | ```
20 |


--------------------------------------------------------------------------------
/commands/publish.md:
--------------------------------------------------------------------------------
1 | Posts a message to the given channel.
2 |
3 | In a Valkey Cluster clients can publish to every node. The cluster makes sure
4 | that published messages are forwarded as needed, so clients can subscribe to any
5 | channel by connecting to any one of the nodes.
6 |


--------------------------------------------------------------------------------
/commands/pubsub-channels.md:
--------------------------------------------------------------------------------
1 | Lists the currently *active channels*.
2 |
3 | An active channel is a Pub/Sub channel with one or more subscribers (excluding clients subscribed to patterns).
4 |
5 | If no `pattern` is specified, all the channels are listed, otherwise if pattern is specified only channels matching the specified glob-style pattern are listed.
6 |
7 | Cluster note: in a Valkey Cluster clients can subscribe to every node, and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, `PUBSUB`'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.
8 |


--------------------------------------------------------------------------------
/commands/pubsub-help.md:
--------------------------------------------------------------------------------
1 | The `PUBSUB HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/pubsub-numpat.md:
--------------------------------------------------------------------------------
1 | Returns the number of unique patterns that are subscribed to by clients (that are performed using the `PSUBSCRIBE` command).
2 |
3 | Note that this isn't the count of clients subscribed to patterns, but the total number of unique patterns all the clients are subscribed to.
4 |
5 | Cluster note: in a Valkey Cluster clients can subscribe to every node, and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, `PUBSUB`'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.
6 |


--------------------------------------------------------------------------------
/commands/pubsub-numsub.md:
--------------------------------------------------------------------------------
1 | Returns the number of subscribers (exclusive of clients subscribed to patterns) for the specified channels.
2 |
3 | Note that it is valid to call this command without channels. In this case it will just return an empty list.
4 |
5 | Cluster note: in a Valkey Cluster clients can subscribe to every node, and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, `PUBSUB`'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.
6 |


--------------------------------------------------------------------------------
/commands/pubsub-shardchannels.md:
--------------------------------------------------------------------------------
 1 | Lists the currently *active shard channels*.
 2 |
 3 | An active shard channel is a Pub/Sub shard channel with one or more subscribers.
 4 |
 5 | If no `pattern` is specified, all the channels are listed, otherwise if pattern is specified only channels matching the specified glob-style pattern are listed.
 6 |
 7 | The information returned about the active shard channels are at the shard level and not at the cluster level.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | > PUBSUB SHARDCHANNELS
13 | 1) "orders"
14 | > PUBSUB SHARDCHANNELS o*
15 | 1) "orders"
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/pubsub-shardnumsub.md:
--------------------------------------------------------------------------------
 1 | Returns the number of subscribers for the specified shard channels.
 2 |
 3 | Note that it is valid to call this command without channels, in this case it will just return an empty list.
 4 |
 5 | Cluster note: in a Valkey Cluster, `PUBSUB`'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | > PUBSUB SHARDNUMSUB orders
11 | 1) "orders"
12 | 2) (integer) 1
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/pubsub.md:
--------------------------------------------------------------------------------
1 | This is a container command for Pub/Sub introspection commands.
2 |
3 | To see the list of available commands you can call `PUBSUB HELP`.
4 |


--------------------------------------------------------------------------------
/commands/punsubscribe.md:
--------------------------------------------------------------------------------
1 | Unsubscribes the client from the given patterns, or from all of them if none is
2 | given.
3 |
4 | When no patterns are specified, the client is unsubscribed from all the
5 | previously subscribed patterns.
6 | In this case, a message for every unsubscribed pattern will be sent to the
7 | client.
8 |


--------------------------------------------------------------------------------
/commands/quit.md:
--------------------------------------------------------------------------------
1 | Ask the server to close the connection.
2 | The connection is closed as soon as all pending replies have been written to the
3 | client.
4 |
5 | **Note:** Clients should not use this command.
6 | Instead, clients should simply close the connection when they're not used anymore.
7 | Terminating a connection on the client side is preferable, as it eliminates `TIME_WAIT` lingering sockets on the server side.
8 |


--------------------------------------------------------------------------------
/commands/randomkey.md:
--------------------------------------------------------------------------------
1 | Return a random key from the currently selected database.
2 |


--------------------------------------------------------------------------------
/commands/readwrite.md:
--------------------------------------------------------------------------------
 1 | Disables read queries for a connection to a Valkey replica node.
 2 |
 3 | Read queries against a Valkey Cluster replica node are disabled by default.
 4 |
 5 | For standalone replica nodes, since Valkey 8.0, read queries are also disabled
 6 | for clients that have executed the `CLIENT CAPA redirect` command.
 7 |
 8 | But you can use the `READONLY` command to change this behavior on a per-
 9 | connection basis. The `READWRITE` command resets the readonly mode flag
10 | of a connection back to readwrite.
11 |


--------------------------------------------------------------------------------
/commands/rename.md:
--------------------------------------------------------------------------------
 1 | Renames `key` to `newkey`.
 2 | It returns an error when `key` does not exist.
 3 | If `newkey` already exists it is overwritten, when this happens `RENAME` executes an implicit `DEL` operation, so if the deleted key contains a very big value it may cause high latency even if `RENAME` itself is usually a constant-time operation.
 4 |
 5 | In Cluster mode, both `key` and `newkey` must be in the same **hash slot**, meaning that in practice only keys that have the same hash tag can be reliably renamed in cluster.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> SET mykey "Hello"
11 | OK
12 | 127.0.0.1:6379> RENAME mykey myotherkey
13 | OK
14 | 127.0.0.1:6379> GET myotherkey
15 | "Hello"
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/renamenx.md:
--------------------------------------------------------------------------------
 1 | Renames `key` to `newkey` if `newkey` does not yet exist.
 2 | It returns an error when `key` does not exist.
 3 |
 4 | In Cluster mode, both `key` and `newkey` must be in the same **hash slot**, meaning that in practice only keys that have the same hash tag can be reliably renamed in cluster.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> SET mykey "Hello"
10 | OK
11 | 127.0.0.1:6379> SET myotherkey "World"
12 | OK
13 | 127.0.0.1:6379> RENAMENX mykey myotherkey
14 | (integer) 0
15 | 127.0.0.1:6379> GET myotherkey
16 | "World"
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/replconf.md:
--------------------------------------------------------------------------------
1 | The `REPLCONF` command is an internal command.
2 | It is used by a Valkey primary to configure a connected replica.


--------------------------------------------------------------------------------
/commands/replicaof.md:
--------------------------------------------------------------------------------
 1 | The `REPLICAOF` command can change the replication settings of a replica on the fly.
 2 |
 3 | If a Valkey server is already acting as replica, the command `REPLICAOF` NO ONE will turn off the replication, turning the Valkey server into a PRIMARY.  In the proper form `REPLICAOF` hostname port will make the server a replica of another server listening at the specified hostname and port.
 4 |
 5 | If a server is already a replica of some primary, `REPLICAOF` hostname port will stop the replication against the old server and start the synchronization against the new one, discarding the old dataset.
 6 |
 7 | The form `REPLICAOF` NO ONE will stop replication, turning the server into a MASTER, but will not discard the replication. So, if the old primary stops working, it is possible to turn the replica into a primary and set the application to use this new primary in read/write. Later when the other Valkey server is fixed, it can be reconfigured to work as a replica.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | > REPLICAOF NO ONE
13 | "OK"
14 |
15 | > REPLICAOF 127.0.0.1 6799
16 | "OK"
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/reset.md:
--------------------------------------------------------------------------------
 1 | This command performs a full reset of the connection's server-side context,
 2 | mimicking the effect of disconnecting and reconnecting again.
 3 |
 4 | When the command is called from a regular client connection, it does the
 5 | following:
 6 |
 7 | * Discards the current `MULTI` transaction block, if one exists.
 8 | * Unwatches all keys `WATCH`ed by the connection.
 9 | * Disables `CLIENT TRACKING`, if in use.
10 | * Sets the connection to `READWRITE` mode.
11 | * Cancels the connection's `ASKING` mode, if previously set.
12 | * Sets `CLIENT REPLY` to `ON`.
13 | * Sets the protocol version to RESP2.
14 | * `SELECT`s database 0.
15 | * Exits `MONITOR` mode, when applicable.
16 | * Aborts Pub/Sub's subscription state (`SUBSCRIBE` and `PSUBSCRIBE`), when
17 |   appropriate.
18 | * Deauthenticates the connection, requiring a call `AUTH` to reauthenticate when
19 |   authentication is enabled.
20 | * Turns off `NO-EVICT` mode.
21 | * Turns off `NO-TOUCH` mode.
22 |


--------------------------------------------------------------------------------
/commands/restore-asking.md:
--------------------------------------------------------------------------------
1 | The `RESTORE-ASKING` command is an internal command.
2 | It is used by a Valkey cluster primary during slot migration.


--------------------------------------------------------------------------------
/commands/restore.md:
--------------------------------------------------------------------------------
 1 | Create a key associated with a value that is obtained by deserializing the
 2 | provided serialized value (obtained via `DUMP`).
 3 |
 4 | If `ttl` is 0 the key is created without any expire, otherwise the specified
 5 | expire time (in milliseconds) is set.
 6 |
 7 | If the `ABSTTL` modifier was used, `ttl` should represent an absolute
 8 | [Unix timestamp][hewowu] (in milliseconds) in which the key will expire.
 9 |
10 | [hewowu]: http://en.wikipedia.org/wiki/Unix_time
11 |
12 | For eviction purposes, you may use the `IDLETIME` or `FREQ` modifiers. See
13 | `OBJECT` for more information.
14 |
15 | `!RESTORE` will return a "Target key name is busy" error when `key` already
16 | exists unless you use the `REPLACE` modifier.
17 |
18 | `!RESTORE` checks the RDB version and data checksum.
19 | If they don't match an error is returned.
20 |
21 | ## Examples
22 |
23 | ```
24 | 127.0.0.1:6379> DEL mykey
25 | (integer) 0
26 | 127.0.0.1:6379> RESTORE mykey 0 "\n\x17\x17\x00\x00\x00\x12\x00\x00\x00\x03\x00\
27 |                         x00\xc0\x01\x00\x04\xc0\x02\x00\x04\xc0\x03\x00\
28 |                         xff\x04\x00u#<\xc0;.\xe9\xdd"
29 | OK
30 | 127.0.0.1:6379> TYPE mykey
31 | list
32 | 127.0.0.1:6379> LRANGE mykey 0 -1
33 | 1) "1"
34 | 2) "2"
35 | 3) "3"
36 | ```
37 |


--------------------------------------------------------------------------------
/commands/rpop.md:
--------------------------------------------------------------------------------
 1 | Removes and returns the last elements of the list stored at `key`.
 2 |
 3 | By default, the command pops a single element from the end of the list.
 4 | When provided with the optional `count` argument, the reply will consist of up
 5 | to `count` elements, depending on the list's length.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> RPUSH mylist "one" "two" "three" "four" "five"
11 | (integer) 5
12 | 127.0.0.1:6379> RPOP mylist
13 | "five"
14 | 127.0.0.1:6379> RPOP mylist 2
15 | 1) "four"
16 | 2) "three"
17 | 127.0.0.1:6379> LRANGE mylist 0 -1
18 | 1) "one"
19 | 2) "two"
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/rpush.md:
--------------------------------------------------------------------------------
 1 | Insert all the specified values at the tail of the list stored at `key`.
 2 | If `key` does not exist, it is created as empty list before performing the push
 3 | operation.
 4 | When `key` holds a value that is not a list, an error is returned.
 5 |
 6 | It is possible to push multiple elements using a single command call just
 7 | specifying multiple arguments at the end of the command.
 8 | Elements are inserted one after the other to the tail of the list, from the
 9 | leftmost element to the rightmost element.
10 | So for instance the command `RPUSH mylist a b c` will result into a list
11 | containing `a` as first element, `b` as second element and `c` as third element.
12 |
13 | ## Examples
14 |
15 | ```
16 | 127.0.0.1:6379> RPUSH mylist "hello"
17 | (integer) 1
18 | 127.0.0.1:6379> RPUSH mylist "world"
19 | (integer) 2
20 | 127.0.0.1:6379> LRANGE mylist 0 -1
21 | 1) "hello"
22 | 2) "world"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/rpushx.md:
--------------------------------------------------------------------------------
 1 | Inserts specified values at the tail of the list stored at `key`, only if `key`
 2 | already exists and holds a list.
 3 | In contrary to `RPUSH`, no operation will be performed when `key` does not yet
 4 | exist.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> RPUSH mylist "Hello"
10 | (integer) 1
11 | 127.0.0.1:6379> RPUSHX mylist "World"
12 | (integer) 2
13 | 127.0.0.1:6379> RPUSHX myotherlist "World"
14 | (integer) 0
15 | 127.0.0.1:6379> LRANGE mylist 0 -1
16 | 1) "Hello"
17 | 2) "World"
18 | 127.0.0.1:6379> LRANGE myotherlist 0 -1
19 | (empty array)
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/sadd.md:
--------------------------------------------------------------------------------
 1 | Add the specified members to the set stored at `key`.
 2 | Specified members that are already a member of this set are ignored.
 3 | If `key` does not exist, a new set is created before adding the specified
 4 | members.
 5 |
 6 | An error is returned when the value stored at `key` is not a set.
 7 |
 8 | ## Examples
 9 |
10 | ```
11 | 127.0.0.1:6379> SADD myset "Hello"
12 | (integer) 1
13 | 127.0.0.1:6379> SADD myset "World"
14 | (integer) 1
15 | 127.0.0.1:6379> SADD myset "World"
16 | (integer) 0
17 | 127.0.0.1:6379> SMEMBERS myset
18 | 1) "Hello"
19 | 2) "World"
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/save.md:
--------------------------------------------------------------------------------
 1 | The `SAVE` commands performs a **synchronous** save of the dataset producing a
 2 | _point in time_ snapshot of all the data inside the Valkey instance, in the form
 3 | of an RDB file.
 4 |
 5 | You almost never want to call `SAVE` in production environments where it will
 6 | block all the other clients.
 7 | Instead usually `BGSAVE` is used.
 8 | However in case of issues preventing Valkey to create the background saving child
 9 | (for instance errors in the fork(2) system call), the `SAVE` command can be a
10 | good last resort to perform the dump of the latest dataset.
11 |
12 | Please refer to the [persistence documentation][tp] for detailed information.
13 |
14 | [tp]: ../topics/persistence.md
15 |


--------------------------------------------------------------------------------
/commands/scard.md:
--------------------------------------------------------------------------------
 1 | Returns the set cardinality (number of elements) of the set stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> SADD myset "Hello"
 7 | (integer) 1
 8 | 127.0.0.1:6379> SADD myset "World"
 9 | (integer) 1
10 | 127.0.0.1:6379> SCARD myset
11 | (integer) 2
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/script-debug.md:
--------------------------------------------------------------------------------
 1 | Set the debug mode for subsequent scripts executed with `EVAL`. Valkey includes a
 2 | complete Lua debugger, codename LDB, that can be used to make the task of
 3 | writing complex scripts much simpler. In debug mode Valkey acts as a remote
 4 | debugging server and a client, such as `valkey-cli`, can execute scripts step by
 5 | step, set breakpoints, inspect variables and more - for additional information
 6 | about LDB refer to the [Valkey Lua debugger](../topics/ldb.md) page.
 7 |
 8 | **Important note:** avoid debugging Lua scripts using your Valkey production
 9 | server. Use a development server instead.
10 |
11 | LDB can be enabled in one of two modes: asynchronous or synchronous. In
12 | asynchronous mode the server creates a forked debugging session that does not
13 | block and all changes to the data are **rolled back** after the session
14 | finishes, so debugging can be restarted using the same initial state. The
15 | alternative synchronous debug mode blocks the server while the debugging session
16 | is active and retains all changes to the data set once it ends.
17 |
18 | * `YES`. Enable non-blocking asynchronous debugging of Lua scripts (changes are discarded).
19 | * `!SYNC`. Enable blocking synchronous debugging of Lua scripts (saves changes to data).
20 | * `NO`. Disables scripts debug mode.
21 |
22 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
23 |


--------------------------------------------------------------------------------
/commands/script-exists.md:
--------------------------------------------------------------------------------
 1 | Returns information about the existence of the scripts in the script cache.
 2 |
 3 | This command accepts one or more SHA1 digests and returns a list of ones or
 4 | zeros to signal if the scripts are already defined or not inside the script
 5 | cache.
 6 | This can be useful before a pipelining operation to ensure that scripts are
 7 | loaded (and if not, to load them using `SCRIPT LOAD`) so that the pipelining
 8 | operation can be performed solely using `EVALSHA` instead of `EVAL` to save
 9 | bandwidth.
10 |
11 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
12 |


--------------------------------------------------------------------------------
/commands/script-flush.md:
--------------------------------------------------------------------------------
 1 | Flush the Lua scripts cache.
 2 |
 3 | By default, `SCRIPT FLUSH` will synchronously flush the cache.
 4 | Setting the **lazyfree-lazy-user-flush** configuration directive to "yes" changes the default flush mode to asynchronous.
 5 |
 6 | It is possible to use one of the following modifiers to dictate the flushing mode explicitly:
 7 |
 8 | * `ASYNC`: flushes the cache asynchronously
 9 | * `!SYNC`: flushes the cache synchronously
10 |
11 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
12 |


--------------------------------------------------------------------------------
/commands/script-help.md:
--------------------------------------------------------------------------------
1 | The `SCRIPT HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/script-kill.md:
--------------------------------------------------------------------------------
 1 | Kills the currently executing `EVAL` script, assuming no write operation was yet
 2 | performed by the script.
 3 |
 4 | This command is mainly useful to kill a script that is running for too much
 5 | time(for instance, because it entered an infinite loop because of a bug).
 6 | The script will be killed, and the client currently blocked into EVAL will see
 7 | the command returning with an error.
 8 |
 9 | If the script has already performed write operations, it can not be killed in this
10 | way because it would violate Lua's script atomicity contract.
11 | In such a case, only `SHUTDOWN NOSAVE` can kill the script, killing
12 | the Valkey process in a hard way and preventing it from persisting with half-written
13 | information.
14 |
15 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
16 |


--------------------------------------------------------------------------------
/commands/script-load.md:
--------------------------------------------------------------------------------
 1 | Load a script into the scripts cache, without executing it.
 2 | After the specified command is loaded into the script cache it will be callable
 3 | using `EVALSHA` with the correct SHA1 digest of the script, exactly like after
 4 | the first successful invocation of `EVAL`.
 5 |
 6 | The script is guaranteed to stay in the script cache forever (unless `SCRIPT
 7 | FLUSH` is called).
 8 |
 9 | The command works in the same way even if the script was already present in the
10 | script cache.
11 |
12 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
13 |


--------------------------------------------------------------------------------
/commands/script-show.md:
--------------------------------------------------------------------------------
1 | Returns the original source code of a script in the script cache.
2 |
3 | This command accepts a SHA1 digest and returns the original script's source code if the script is present in the script cache.
4 | It is intended primary for debugging, allowing users to introspect the contents of a script when they do not have direct access to it.
5 | For example, an admin may only have access to a script's SHA1 from the monitor or slowlog and needs to determine the script's contents for debugging.
6 |
7 | For more information about `EVAL` scripts please refer to [Introduction to Eval Scripts](../topics/eval-intro.md).
8 |


--------------------------------------------------------------------------------
/commands/script.md:
--------------------------------------------------------------------------------
1 | This is a container command for script management commands.
2 |
3 | To see the list of available commands you can call `SCRIPT HELP`.
4 |


--------------------------------------------------------------------------------
/commands/sdiff.md:
--------------------------------------------------------------------------------
 1 | Returns the members of the set resulting from the difference between the first
 2 | set and all the successive sets.
 3 |
 4 | For example:
 5 |
 6 | ```
 7 | key1 = {a,b,c,d}
 8 | key2 = {c}
 9 | key3 = {a,c,e}
10 | SDIFF key1 key2 key3 = {b,d}
11 | ```
12 |
13 | Keys that do not exist are considered to be empty sets.
14 |
15 | ## Examples
16 |
17 | ```
18 | 127.0.0.1:6379> SADD key1 "a"
19 | (integer) 1
20 | 127.0.0.1:6379> SADD key1 "b"
21 | (integer) 1
22 | 127.0.0.1:6379> SADD key1 "c"
23 | (integer) 1
24 | 127.0.0.1:6379> SADD key2 "c"
25 | (integer) 1
26 | 127.0.0.1:6379> SADD key2 "d"
27 | (integer) 1
28 | 127.0.0.1:6379> SADD key2 "e"
29 | (integer) 1
30 | 127.0.0.1:6379> SDIFF key1 key2
31 | 1) "a"
32 | 2) "b"
33 | ```
34 |


--------------------------------------------------------------------------------
/commands/sdiffstore.md:
--------------------------------------------------------------------------------
 1 | This command is equal to `SDIFF`, but instead of returning the resulting set, it
 2 | is stored in `destination`.
 3 |
 4 | If `destination` already exists, it is overwritten.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> SADD key1 "a"
10 | (integer) 1
11 | 127.0.0.1:6379> SADD key1 "b"
12 | (integer) 1
13 | 127.0.0.1:6379> SADD key1 "c"
14 | (integer) 1
15 | 127.0.0.1:6379> SADD key2 "c"
16 | (integer) 1
17 | 127.0.0.1:6379> SADD key2 "d"
18 | (integer) 1
19 | 127.0.0.1:6379> SADD key2 "e"
20 | (integer) 1
21 | 127.0.0.1:6379> SDIFFSTORE key key1 key2
22 | (integer) 2
23 | 127.0.0.1:6379> SMEMBERS key
24 | 1) "a"
25 | 2) "b"
26 | ```
27 |


--------------------------------------------------------------------------------
/commands/select.md:
--------------------------------------------------------------------------------
 1 | Select the Valkey logical database having the specified zero-based numeric index.
 2 | New connections always use the database 0.
 3 |
 4 | Selectable Valkey databases are a form of namespacing: all databases are still persisted in the same RDB / AOF file. However different databases can have keys with the same name, and commands like `FLUSHDB`, `SWAPDB` or `RANDOMKEY` work on specific databases.
 5 |
 6 | In practical terms, Valkey databases should be used to separate different keys belonging to the same application (if needed), and not to use a single Valkey instance for multiple unrelated applications.
 7 |
 8 | When using Valkey Cluster, only `SELECT 0` can be used, since Valkey Cluster only supports database zero. In the case of a Valkey Cluster, having multiple databases would be useless and an unnecessary source of complexity. Commands operating atomically on a single database would not be possible with the Valkey Cluster design and goals.
 9 |
10 | Since the currently selected database is a property of the connection, clients should track the currently selected database and re-select it on reconnection. While there is no command in order to query the selected database in the current connection, the `CLIENT LIST` output shows, for each client, the currently selected database.
11 |


--------------------------------------------------------------------------------
/commands/setex.md:
--------------------------------------------------------------------------------
 1 | Set `key` to hold the string `value` and set `key` to timeout after a given
 2 | number of seconds.
 3 | This command is equivalent to:
 4 |
 5 | ```
 6 | SET key value EX seconds
 7 | ```
 8 |
 9 | An error is returned when `seconds` is invalid.
10 |
11 | ## Examples
12 |
13 | ```
14 | 127.0.0.1:6379> SETEX mykey 10 "Hello"
15 | OK
16 | 127.0.0.1:6379> TTL mykey
17 | (integer) 10
18 | 127.0.0.1:6379> GET mykey
19 | "Hello"
20 | ```
21 | ## See also
22 |
23 | `TTL`


--------------------------------------------------------------------------------
/commands/sinter.md:
--------------------------------------------------------------------------------
 1 | Returns the members of the set resulting from the intersection of all the given
 2 | sets.
 3 |
 4 | For example:
 5 |
 6 | ```
 7 | key1 = {a,b,c,d}
 8 | key2 = {c}
 9 | key3 = {a,c,e}
10 | SINTER key1 key2 key3 = {c}
11 | ```
12 |
13 | Keys that do not exist are considered to be empty sets.
14 | With one of the keys being an empty set, the resulting set is also empty (since
15 | set intersection with an empty set always results in an empty set).
16 |
17 | ## Examples
18 |
19 | ```
20 | 127.0.0.1:6379> SADD key1 "a"
21 | (integer) 1
22 | 127.0.0.1:6379> SADD key1 "b"
23 | (integer) 1
24 | 127.0.0.1:6379> SADD key1 "c"
25 | (integer) 1
26 | 127.0.0.1:6379> SADD key2 "c"
27 | (integer) 1
28 | 127.0.0.1:6379> SADD key2 "d"
29 | (integer) 1
30 | 127.0.0.1:6379> SADD key2 "e"
31 | (integer) 1
32 | 127.0.0.1:6379> SINTER key1 key2
33 | 1) "c"
34 | ```
35 |


--------------------------------------------------------------------------------
/commands/sinterstore.md:
--------------------------------------------------------------------------------
 1 | This command is equal to `SINTER`, but instead of returning the resulting set,
 2 | it is stored in `destination`.
 3 |
 4 | If `destination` already exists, it is overwritten.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> SADD key1 "a"
10 | (integer) 1
11 | 127.0.0.1:6379> SADD key1 "b"
12 | (integer) 1
13 | 127.0.0.1:6379> SADD key1 "c"
14 | (integer) 1
15 | 127.0.0.1:6379> SADD key2 "c"
16 | (integer) 1
17 | 127.0.0.1:6379> SADD key2 "d"
18 | (integer) 1
19 | 127.0.0.1:6379> SADD key2 "e"
20 | (integer) 1
21 | 127.0.0.1:6379> SINTERSTORE key key1 key2
22 | (integer) 1
23 | 127.0.0.1:6379> SMEMBERS key
24 | 1) "c"
25 | ```
26 |


--------------------------------------------------------------------------------
/commands/sismember.md:
--------------------------------------------------------------------------------
 1 | Returns if `member` is a member of the set stored at `key`.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> SADD myset "one"
 7 | (integer) 1
 8 | 127.0.0.1:6379> SISMEMBER myset "one"
 9 | (integer) 1
10 | 127.0.0.1:6379> SISMEMBER myset "two"
11 | (integer) 0
12 | ```
13 |


--------------------------------------------------------------------------------
/commands/slaveof.md:
--------------------------------------------------------------------------------
 1 | **A note about the word slave used in this man page and command name**: If not for backward compatibility, the Valkey project no longer uses the words "master" and "slave". Please use the new command `REPLICAOF`. The command `SLAVEOF` will continue to work for backward compatibility.
 2 |
 3 | The `SLAVEOF` command can change the replication settings of a replica on the fly.
 4 | If a Valkey server is already acting as replica, the command `SLAVEOF` NO ONE will
 5 | turn off the replication, turning the Valkey server into a MASTER.
 6 | In the proper form `SLAVEOF` hostname port will make the server a replica of
 7 | another server listening at the specified hostname and port.
 8 |
 9 | If a server is already a replica of some primary, `SLAVEOF` hostname port will stop
10 | the replication against the old server and start the synchronization against the
11 | new one, discarding the old dataset.
12 |
13 | The form `SLAVEOF` NO ONE will stop replication, turning the server into a
14 | MASTER, but will not discard the replication.
15 | So, if the old primary stops working, it is possible to turn the replica into a
16 | primary and set the application to use this new primary in read/write.
17 | Later when the other Valkey server is fixed, it can be reconfigured to work as a
18 | replica.
19 |


--------------------------------------------------------------------------------
/commands/slowlog-help.md:
--------------------------------------------------------------------------------
1 | The `SLOWLOG HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/slowlog-len.md:
--------------------------------------------------------------------------------
1 | This command returns the current number of entries in the slow log.
2 |
3 | A new entry is added to the slow log whenever a command exceeds the execution time threshold defined by the `slowlog-log-slower-than` configuration directive.
4 | The maximum number of entries in the slow log is governed by the `slowlog-max-len` configuration directive.
5 | Once the slog log reaches its maximal size, the oldest entry is removed whenever a new entry is created.
6 | The slow log can be cleared with the `SLOWLOG RESET` command.
7 |


--------------------------------------------------------------------------------
/commands/slowlog-reset.md:
--------------------------------------------------------------------------------
1 | This command resets the slow log, clearing all entries in it.
2 |
3 | Once deleted the information is lost forever.
4 |


--------------------------------------------------------------------------------
/commands/slowlog.md:
--------------------------------------------------------------------------------
1 | This is a container command for slow log management commands.
2 |
3 | To see the list of available commands you can call `SLOWLOG HELP`.
4 |


--------------------------------------------------------------------------------
/commands/smembers.md:
--------------------------------------------------------------------------------
 1 | Returns all the members of the set value stored at `key`.
 2 |
 3 | This has the same effect as running `SINTER` with one argument `key`.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> SADD myset "Hello"
 9 | (integer) 1
10 | 127.0.0.1:6379> SADD myset "World"
11 | (integer) 1
12 | 127.0.0.1:6379> SMEMBERS myset
13 | 1) "Hello"
14 | 2) "World"
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/smismember.md:
--------------------------------------------------------------------------------
 1 | Returns whether each `member` is a member of the set stored at `key`.
 2 |
 3 | For every `member`, `1` is returned if the value is a member of the set, or `0` if the element is not a member of the set or if `key` does not exist.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> SADD myset "one"
 9 | (integer) 1
10 | 127.0.0.1:6379> SADD myset "one"
11 | (integer) 0
12 | 127.0.0.1:6379> SMISMEMBER myset "one" "notamember"
13 | 1) (integer) 1
14 | 2) (integer) 0
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/smove.md:
--------------------------------------------------------------------------------
 1 | Move `member` from the set at `source` to the set at `destination`.
 2 | This operation is atomic.
 3 | In every given moment the element will appear to be a member of `source` **or**
 4 | `destination` for other clients.
 5 |
 6 | If the source set does not exist or does not contain the specified element, no
 7 | operation is performed and `0` is returned.
 8 | Otherwise, the element is removed from the source set and added to the
 9 | destination set.
10 | When the specified element already exists in the destination set, it is only
11 | removed from the source set.
12 |
13 | An error is returned if `source` or `destination` does not hold a set value.
14 |
15 | ## Examples
16 |
17 | ```
18 | 127.0.0.1:6379> SADD myset "one"
19 | (integer) 1
20 | 127.0.0.1:6379> SADD myset "two"
21 | (integer) 1
22 | 127.0.0.1:6379> SADD myotherset "three"
23 | (integer) 1
24 | 127.0.0.1:6379> SMOVE myset myotherset "two"
25 | (integer) 1
26 | 127.0.0.1:6379> SMEMBERS myset
27 | 1) "one"
28 | 127.0.0.1:6379> SMEMBERS myotherset
29 | 1) "three"
30 | 2) "two"
31 | ```
32 |


--------------------------------------------------------------------------------
/commands/sort_ro.md:
--------------------------------------------------------------------------------
 1 | Read-only variant of the `SORT` command. It is exactly like the original `SORT` but refuses the `STORE` option and can safely be used in read-only replicas.
 2 |
 3 | Since the original `SORT` has a `STORE` option it is technically flagged as a writing command in the Valkey command table. For this reason read-only replicas in a Valkey Cluster will redirect it to the primary instance even if the connection is in read-only mode (see the `READONLY` command of Valkey Cluster).
 4 |
 5 | The `SORT_RO` variant was introduced in order to allow `SORT` behavior in read-only replicas without breaking compatibility on command flags.
 6 |
 7 | See original `SORT` for more details.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | SORT_RO mylist BY weight_*->fieldname GET object_*->fieldname
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/spop.md:
--------------------------------------------------------------------------------
 1 | Removes and returns one or more random members from the set value store at `key`.
 2 |
 3 | This operation is similar to `SRANDMEMBER`, that returns one or more random elements from a set but does not remove it.
 4 |
 5 | By default, the command pops a single member from the set. When provided with
 6 | the optional `count` argument, the reply will consist of up to `count` members,
 7 | depending on the set's cardinality.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> SADD myset "one"
13 | (integer) 1
14 | 127.0.0.1:6379> SADD myset "two"
15 | (integer) 1
16 | 127.0.0.1:6379> SADD myset "three"
17 | (integer) 1
18 | 127.0.0.1:6379> SPOP myset
19 | "three"
20 | 127.0.0.1:6379> SMEMBERS myset
21 | 1) "one"
22 | 2) "two"
23 | 127.0.0.1:6379> SADD myset "four"
24 | (integer) 1
25 | 127.0.0.1:6379> SADD myset "five"
26 | (integer) 1
27 | 127.0.0.1:6379> SPOP myset 3
28 | 1) "one"
29 | 2) "four"
30 | 3) "five"
31 | 127.0.0.1:6379> SMEMBERS myset
32 | 1) "two"
33 | ```
34 | ## Distribution of returned elements
35 |
36 | Note that this command is not suitable when you need a guaranteed uniform distribution of the returned elements. For more information about the algorithms used for `SPOP`, look up both the Knuth sampling and Floyd sampling algorithms.
37 |


--------------------------------------------------------------------------------
/commands/spublish.md:
--------------------------------------------------------------------------------
 1 | Posts a message to the given shard channel.
 2 |
 3 | In Valkey Cluster, shard channels are assigned to slots by the same algorithm used to assign keys to slots.
 4 | A shard message must be sent to a node that own the slot the shard channel is hashed to.
 5 | The cluster makes sure that published shard messages are forwarded to all the node in the shard, so clients can subscribe to a shard channel by connecting to any one of the nodes in the shard.
 6 |
 7 | For more information about sharded pubsub, see [Sharded Pubsub](../topics/pubsub.md#sharded-pubsub).
 8 |
 9 | ## Examples
10 |
11 | For example the following command publish to channel `orders` with a subscriber already waiting for message(s).
12 |
13 | ```
14 | > spublish orders hello
15 | (integer) 1
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/srem.md:
--------------------------------------------------------------------------------
 1 | Remove the specified members from the set stored at `key`.
 2 | Specified members that are not a member of this set are ignored.
 3 | If `key` does not exist, it is treated as an empty set and this command returns
 4 | `0`.
 5 |
 6 | An error is returned when the value stored at `key` is not a set.
 7 |
 8 | ## Examples
 9 |
10 | ```
11 | 127.0.0.1:6379> SADD myset "one"
12 | (integer) 1
13 | 127.0.0.1:6379> SADD myset "two"
14 | (integer) 1
15 | 127.0.0.1:6379> SADD myset "three"
16 | (integer) 1
17 | 127.0.0.1:6379> SREM myset "one"
18 | (integer) 1
19 | 127.0.0.1:6379> SREM myset "four"
20 | (integer) 0
21 | 127.0.0.1:6379> SMEMBERS myset
22 | 1) "two"
23 | 2) "three"
24 | ```
25 |


--------------------------------------------------------------------------------
/commands/sscan.md:
--------------------------------------------------------------------------------
1 | See `SCAN` for `SSCAN` documentation.
2 |


--------------------------------------------------------------------------------
/commands/ssubscribe.md:
--------------------------------------------------------------------------------
 1 | Subscribes the client to the specified shard channels.
 2 |
 3 | In a Valkey cluster, shard channels are assigned to slots by the same algorithm used to assign keys to slots.
 4 | Client(s) can subscribe to a node covering a slot (primary/replica) to receive the messages published.
 5 | All the specified shard channels needs to belong to a single slot to subscribe in a given `SSUBSCRIBE` call,
 6 | A client can subscribe to channels across different slots over separate `SSUBSCRIBE` call.
 7 |
 8 | For more information about sharded Pub/Sub, see [Sharded Pub/Sub](../topics/pubsub.md#sharded-pubsub).
 9 |
10 | ## Examples
11 |
12 | ```
13 | > ssubscribe orders
14 | Reading messages... (press Ctrl-C to quit)
15 | 1) "ssubscribe"
16 | 2) "orders"
17 | 3) (integer) 1
18 | 1) "smessage"
19 | 2) "orders"
20 | 3) "hello"
21 | ```
22 |


--------------------------------------------------------------------------------
/commands/strlen.md:
--------------------------------------------------------------------------------
 1 | Returns the length of the string value stored at `key`.
 2 | An error is returned when `key` holds a non-string value.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> SET mykey "Hello world"
 8 | OK
 9 | 127.0.0.1:6379> STRLEN mykey
10 | (integer) 11
11 | 127.0.0.1:6379> STRLEN nonexisting
12 | (integer) 0
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/subscribe.md:
--------------------------------------------------------------------------------
 1 | Subscribes the client to the specified channels.
 2 |
 3 | Once the client enters the subscribed state it is not supposed to issue any
 4 | other commands, except for additional `SUBSCRIBE`, `SSUBSCRIBE`, `PSUBSCRIBE`, `UNSUBSCRIBE`, `SUNSUBSCRIBE`,
 5 | `PUNSUBSCRIBE`, `PING`, `RESET` and `QUIT` commands.
 6 | However, if RESP3 is used (see `HELLO`) it is possible for a client to issue any commands while in subscribed state.
 7 |
 8 | Note that `RESET` can be called to exit subscribed state.
 9 |
10 | For more information, see [Pub/sub](../topics/pubsub.md).
11 |
12 |


--------------------------------------------------------------------------------
/commands/substr.md:
--------------------------------------------------------------------------------
 1 | Returns the substring of the string value stored at `key`, determined by the
 2 | offsets `start` and `end` (both are inclusive).
 3 | Negative offsets can be used in order to provide an offset starting from the end
 4 | of the string.
 5 | So -1 means the last character, -2 the penultimate and so forth.
 6 |
 7 | The function handles out of range requests by limiting the resulting range to
 8 | the actual length of the string.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> SET mykey "This is a string"
14 | OK
15 | 127.0.0.1:6379> GETRANGE mykey 0 3
16 | "This"
17 | 127.0.0.1:6379> GETRANGE mykey -3 -1
18 | "ing"
19 | 127.0.0.1:6379> GETRANGE mykey 0 -1
20 | "This is a string"
21 | 127.0.0.1:6379> GETRANGE mykey 10 100
22 | "string"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/sunion.md:
--------------------------------------------------------------------------------
 1 | Returns the members of the set resulting from the union of all the given sets.
 2 |
 3 | For example:
 4 |
 5 | ```
 6 | key1 = {a,b,c,d}
 7 | key2 = {c}
 8 | key3 = {a,c,e}
 9 | SUNION key1 key2 key3 = {a,b,c,d,e}
10 | ```
11 |
12 | Keys that do not exist are considered to be empty sets.
13 |
14 | ## Examples
15 |
16 | ```
17 | 127.0.0.1:6379> SADD key1 "a"
18 | (integer) 1
19 | 127.0.0.1:6379> SADD key1 "b"
20 | (integer) 1
21 | 127.0.0.1:6379> SADD key1 "c"
22 | (integer) 1
23 | 127.0.0.1:6379> SADD key2 "c"
24 | (integer) 1
25 | 127.0.0.1:6379> SADD key2 "d"
26 | (integer) 1
27 | 127.0.0.1:6379> SADD key2 "e"
28 | (integer) 1
29 | 127.0.0.1:6379> SUNION key1 key2
30 | 1) "a"
31 | 2) "b"
32 | 3) "c"
33 | 4) "d"
34 | 5) "e"
35 | ```
36 |


--------------------------------------------------------------------------------
/commands/sunionstore.md:
--------------------------------------------------------------------------------
 1 | This command is equal to `SUNION`, but instead of returning the resulting set,
 2 | it is stored in `destination`.
 3 |
 4 | If `destination` already exists, it is overwritten.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> SADD key1 "a"
10 | (integer) 1
11 | 127.0.0.1:6379> SADD key1 "b"
12 | (integer) 1
13 | 127.0.0.1:6379> SADD key1 "c"
14 | (integer) 1
15 | 127.0.0.1:6379> SADD key2 "c"
16 | (integer) 1
17 | 127.0.0.1:6379> SADD key2 "d"
18 | (integer) 1
19 | 127.0.0.1:6379> SADD key2 "e"
20 | (integer) 1
21 | 127.0.0.1:6379> SUNIONSTORE key key1 key2
22 | (integer) 5
23 | 127.0.0.1:6379> SMEMBERS key
24 | 1) "a"
25 | 2) "b"
26 | 3) "c"
27 | 4) "d"
28 | 5) "e"
29 | ```
30 |


--------------------------------------------------------------------------------
/commands/sunsubscribe.md:
--------------------------------------------------------------------------------
1 | Unsubscribes the client from the given shard channels, or from all of them if none is given.
2 |
3 | When no shard channels are specified, the client is unsubscribed from all the previously subscribed shard channels.
4 | In this case a message for every unsubscribed shard channel will be sent to the client.
5 |
6 | Note: The global channels and shard channels needs to be unsubscribed from separately.
7 |
8 | For more information about sharded Pub/Sub, see [Sharded Pub/Sub](../topics/pubsub.md#sharded-pubsub).
9 |


--------------------------------------------------------------------------------
/commands/swapdb.md:
--------------------------------------------------------------------------------
 1 | This command swaps two Valkey databases, so that immediately all the
 2 | clients connected to a given database will see the data of the other database, and
 3 | the other way around. Example:
 4 |
 5 |     SWAPDB 0 1
 6 |
 7 | This will swap database 0 with database 1. All the clients connected with database 0 will immediately see the new data, exactly like all the clients connected with database 1 will see the data that was formerly of database 0.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | SWAPDB 0 1
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/sync.md:
--------------------------------------------------------------------------------
 1 | Initiates a replication stream from the primary.
 2 |
 3 | The `SYNC` command is called by Valkey replicas for initiating a replication
 4 | stream from the primary. It has been replaced in newer versions of Valkey by
 5 |  `PSYNC`.
 6 |
 7 | For more information about replication in Valkey please check the
 8 | [replication page][tr].
 9 |
10 | [tr]: ../topics/replication.md
11 |


--------------------------------------------------------------------------------
/commands/time.md:
--------------------------------------------------------------------------------
 1 | The `TIME` command returns the current server time as a two items lists: a Unix
 2 | timestamp and the amount of microseconds already elapsed in the current second.
 3 | Basically the interface is very similar to the one of the `gettimeofday` system
 4 | call.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> TIME
10 | 1) "1714701491"
11 | 2) "723379"
12 | 127.0.0.1:6379> TIME
13 | 1) "1714701491"
14 | 2) "731773"
15 | ```
16 |


--------------------------------------------------------------------------------
/commands/touch.md:
--------------------------------------------------------------------------------
 1 | Alters the last access time of a key(s).
 2 | A key is ignored if it does not exist.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> SET key1 "Hello"
 8 | OK
 9 | 127.0.0.1:6379> SET key2 "World"
10 | OK
11 | 127.0.0.1:6379> TOUCH key1 key2
12 | (integer) 2
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/ttl.md:
--------------------------------------------------------------------------------
 1 | Returns the remaining time to live of a key that has a timeout.
 2 | This introspection capability allows a Valkey client to check how many seconds a
 3 | given key will continue to be part of the dataset.
 4 |
 5 | The command returns the following values in case of errors:
 6 |
 7 | * The command returns `-2` if the key does not exist.
 8 | * The command returns `-1` if the key exists but has no associated expire.
 9 |
10 | See also the `PTTL` command that returns the same information with milliseconds resolution.
11 |
12 | ## Examples
13 |
14 | ```
15 | 127.0.0.1:6379> SET mykey "Hello"
16 | OK
17 | 127.0.0.1:6379> EXPIRE mykey 10
18 | (integer) 1
19 | 127.0.0.1:6379> TTL mykey
20 | (integer) 10
21 | ```
22 |


--------------------------------------------------------------------------------
/commands/type.md:
--------------------------------------------------------------------------------
 1 | Returns the string representation of the type of the value stored at `key`.
 2 | The different types that can be returned are: `string`, `list`, `set`, `zset`,
 3 | `hash` and `stream`.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> SET key1 "value"
 9 | OK
10 | 127.0.0.1:6379> LPUSH key2 "value"
11 | (integer) 1
12 | 127.0.0.1:6379> SADD key3 "value"
13 | (integer) 1
14 | 127.0.0.1:6379> TYPE key1
15 | string
16 | 127.0.0.1:6379> TYPE key2
17 | list
18 | 127.0.0.1:6379> TYPE key3
19 | set
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/unlink.md:
--------------------------------------------------------------------------------
 1 | This command is very similar to `DEL`: it removes the specified keys.
 2 | Just like `DEL` a key is ignored if it does not exist. However the command
 3 | performs the actual memory reclaiming in a different thread, so it is not
 4 | blocking, while `DEL` is. This is where the command name comes from: the
 5 | command just **unlinks** the keys from the keyspace. The actual removal
 6 | will happen later asynchronously.
 7 |
 8 | ## Examples
 9 |
10 | ```
11 | 127.0.0.1:6379> SET key1 "Hello"
12 | OK
13 | 127.0.0.1:6379> SET key2 "World"
14 | OK
15 | 127.0.0.1:6379> UNLINK key1 key2 key3
16 | (integer) 2
17 | ```
18 |


--------------------------------------------------------------------------------
/commands/unsubscribe.md:
--------------------------------------------------------------------------------
1 | Unsubscribes the client from the given channels, or from all of them if none is
2 | given.
3 |
4 | When no channels are specified, the client is unsubscribed from all the
5 | previously subscribed channels.
6 | In this case, a message for every unsubscribed channel will be sent to the
7 | client.
8 |


--------------------------------------------------------------------------------
/commands/unwatch.md:
--------------------------------------------------------------------------------
1 | Flushes all the previously watched keys for a [transaction][tt].
2 |
3 | [tt]: ../topics/transactions.md
4 |
5 | If you call `EXEC` or `DISCARD`, there's no need to manually call `UNWATCH`.
6 |


--------------------------------------------------------------------------------
/commands/watch.md:
--------------------------------------------------------------------------------
1 | Marks the given keys to be watched for conditional execution of a
2 | [transaction][tt].
3 |
4 | [tt]: ../topics/transactions.md
5 |


--------------------------------------------------------------------------------
/commands/xack.md:
--------------------------------------------------------------------------------
 1 | The `XACK` command removes one or multiple messages from the
 2 | *Pending Entries List* (PEL) of a stream consumer group. A message is pending,
 3 | and as such stored inside the PEL, when it was delivered to some consumer,
 4 | normally as a side effect of calling `XREADGROUP`, or when a consumer took
 5 | ownership of a message calling `XCLAIM`. The pending message was delivered to
 6 | some consumer but the server is yet not sure it was processed at least once.
 7 | So new calls to `XREADGROUP` to grab the messages history for a consumer
 8 | (for instance using an ID of 0), will return such message.
 9 | Similarly the pending message will be listed by the `XPENDING` command,
10 | that inspects the PEL.
11 |
12 | Once a consumer *successfully* processes a message, it should call `XACK`
13 | so that such message does not get processed again, and as a side effect,
14 | the PEL entry about this message is also purged, releasing memory from the
15 | Valkey server.
16 |
17 | ## Examples
18 |
19 | ```
20 | 127.0.0.1:6379> XACK mystream mygroup 1526569495631-0
21 | (integer) 1
22 | ```
23 |


--------------------------------------------------------------------------------
/commands/xgroup-create.md:
--------------------------------------------------------------------------------
 1 | Create a new consumer group uniquely identified by `<groupname>` for the stream stored at `<key>`
 2 |
 3 | Every group has a unique name in a given stream.
 4 | When a consumer group with the same name already exists, the command returns a `-BUSYGROUP` error.
 5 |
 6 | The command's `<id>` argument specifies the last delivered entry in the stream from the new group's perspective.
 7 | The special ID `


































         is the ID of the last entry in the stream, but you can substitute it with any valid ID.
 8 |
 9 | For example, if you want the group's consumers to fetch the entire stream from the beginning, use zero as the starting ID for the consumer group:
10 |
11 |     XGROUP CREATE mystream mygroup 0
12 |
13 | By default, the `XGROUP CREATE` command expects that the target stream exists, and returns an error when it doesn't.
14 | If a stream does not exist, you can create it automatically with length of 0 by using the optional `MKSTREAM` subcommand as the last argument after the `<id>`:
15 |
16 |     XGROUP CREATE mystream mygroup $ MKSTREAM
17 |
18 | To enable consumer group lag tracking, specify the optional `entries_read` named argument with an arbitrary ID.
19 | An arbitrary ID is any ID that isn't the ID of the stream's first entry, last entry, or zero ("0-0") ID.
20 | Use it to find out how many entries are between the arbitrary ID (excluding it) and the stream's last entry.
21 | Set the `entries_read` the stream's `entries_added` subtracted by the number of entries.
22 |


--------------------------------------------------------------------------------
/commands/xgroup-createconsumer.md:
--------------------------------------------------------------------------------
1 | Create a consumer named `<consumername>` in the consumer group `<groupname>` of the stream that's stored at `<key>`.
2 |
3 | Consumers are also created automatically whenever an operation, such as `XREADGROUP`, references a consumer that doesn't exist.
4 | This is valid for `XREADGROUP` only when there is data in the stream.
5 |


--------------------------------------------------------------------------------
/commands/xgroup-delconsumer.md:
--------------------------------------------------------------------------------
1 | The `XGROUP DELCONSUMER` command deletes a consumer from the consumer group.
2 |
3 | Sometimes it may be useful to remove old consumers since they are no longer used.
4 |
5 | Note, however, that any pending messages that the consumer had will become unclaimable after it was deleted.
6 | It is strongly recommended, therefore, that any pending messages are claimed or acknowledged prior to deleting the consumer from the group.
7 |


--------------------------------------------------------------------------------
/commands/xgroup-destroy.md:
--------------------------------------------------------------------------------
1 | The `XGROUP DESTROY` command completely destroys a consumer group.
2 |
3 | The consumer group will be destroyed even if there are active consumers, and pending messages, so make sure to call this command only when really needed.
4 |


--------------------------------------------------------------------------------
/commands/xgroup-help.md:
--------------------------------------------------------------------------------
1 | The `XGROUP HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/xgroup-setid.md:
--------------------------------------------------------------------------------
 1 | Set the **last delivered ID** for a consumer group.
 2 |
 3 | Normally, a consumer group's last delivered ID is set when the group is created with `XGROUP CREATE`.
 4 | The `XGROUP SETID` command allows modifying the group's last delivered ID, without having to delete and recreate the group.
 5 | For instance if you want the consumers in a consumer group to re-process all the messages in a stream, you may want to set its next ID to 0:
 6 |
 7 |     XGROUP SETID mystream mygroup 0
 8 |
 9 | The optional `entries_read` argument can be specified to enable consumer group lag tracking for an arbitrary ID.
10 | An arbitrary ID is any ID that isn't the ID of the stream's first entry, its last entry or the zero ("0-0") ID.
11 | This can be useful you know exactly how many entries are between the arbitrary ID (excluding it) and the stream's last entry.
12 | In such cases, the `entries_read` can be set to the stream's `entries_added` subtracted with the number of entries.
13 |


--------------------------------------------------------------------------------
/commands/xgroup.md:
--------------------------------------------------------------------------------
1 | This is a container command for stream consumer group management commands.
2 |
3 | To see the list of available commands you can call `XGROUP HELP`.
4 |


--------------------------------------------------------------------------------
/commands/xinfo-consumers.md:
--------------------------------------------------------------------------------
 1 | This command returns the list of consumers that belong to the `<groupname>` consumer group of the stream stored at `<key>`.
 2 |
 3 | The following information is provided for each consumer in the group:
 4 |
 5 | * **name**: the consumer's name
 6 | * **pending**: the number of entries in the PEL: pending messages for the consumer, which are messages that were delivered but are yet to be acknowledged
 7 | * **idle**: the number of milliseconds that have passed since the consumer's last attempted interaction (Examples: `XREADGROUP`, `XCLAIM`, `XAUTOCLAIM`)
 8 | * **inactive**: the number of milliseconds that have passed since the consumer's last successful interaction (Examples: `XREADGROUP` that actually read some entries into the PEL, `XCLAIM`/`XAUTOCLAIM` that actually claimed some entries)
 9 |
10 | ## Examples
11 |
12 | ```
13 | > XINFO CONSUMERS mystream mygroup
14 | 1) 1) name
15 |    2) "Alice"
16 |    3) pending
17 |    4) (integer) 1
18 |    5) idle
19 |    6) (integer) 9104628
20 |    7) inactive
21 |    8) (integer) 18104698
22 | 2) 1) name
23 |    2) "Bob"
24 |    3) pending
25 |    4) (integer) 1
26 |    5) idle
27 |    6) (integer) 83841983
28 |    7) inactive
29 |    8) (integer) 993841998
30 | ```
31 |


--------------------------------------------------------------------------------
/commands/xinfo-help.md:
--------------------------------------------------------------------------------
1 | The `XINFO HELP` command returns a helpful text describing the different subcommands.
2 |


--------------------------------------------------------------------------------
/commands/xinfo.md:
--------------------------------------------------------------------------------
1 | This is a container command for stream introspection commands.
2 |
3 | To see the list of available commands you can call `XINFO HELP`.
4 |


--------------------------------------------------------------------------------
/commands/xlen.md:
--------------------------------------------------------------------------------
 1 | Returns the number of entries inside a stream. If the specified key does not
 2 | exist the command returns zero, as if the stream was empty.
 3 | However note that unlike other Valkey types, zero-length streams are
 4 | possible, so you should call `TYPE` or `EXISTS` in order to check if
 5 | a key exists or not.
 6 |
 7 | Streams are not auto-deleted once they have no entries inside (for instance
 8 | after an `XDEL` call), because the stream may have consumer groups
 9 | associated with it.
10 |
11 | ## Examples
12 |
13 | ```
14 | 127.0.0.1:6379> XADD mystream * item 1
15 | "1714701492011-0"
16 | 127.0.0.1:6379> XADD mystream * item 2
17 | "1714701492021-0"
18 | 127.0.0.1:6379> XADD mystream * item 3
19 | "1714701492031-0"
20 | 127.0.0.1:6379> XLEN mystream
21 | (integer) 3
22 | ```
23 |


--------------------------------------------------------------------------------
/commands/xrevrange.md:
--------------------------------------------------------------------------------
 1 | This command is exactly like `XRANGE`, but with the notable difference of
 2 | returning the entries in reverse order, and also taking the start-end
 3 | range in reverse order: in `XREVRANGE` you need to state the *end* ID
 4 | and later the *start* ID, and the command will produce all the element
 5 | between (or exactly like) the two IDs, starting from the *end* side.
 6 |
 7 | So for instance, to get all the elements from the higher ID to the lower
 8 | ID one could use:
 9 |
10 |     XREVRANGE somestream + -
11 |
12 | Similarly to get just the last element added into the stream it is
13 | enough to send:
14 |
15 |     XREVRANGE somestream + - COUNT 1
16 |
17 | ## Examples
18 |
19 | ```
20 | 127.0.0.1:6379> XADD writers * name Virginia surname Woolf
21 | "1714701492147-0"
22 | 127.0.0.1:6379> XADD writers * name Jane surname Austen
23 | "1714701492157-0"
24 | 127.0.0.1:6379> XADD writers * name Toni surname Morrison
25 | "1714701492167-0"
26 | 127.0.0.1:6379> XADD writers * name Agatha surname Christie
27 | "1714701492177-0"
28 | 127.0.0.1:6379> XADD writers * name Ngozi surname Adichie
29 | "1714701492187-0"
30 | 127.0.0.1:6379> XLEN writers
31 | (integer) 5
32 | 127.0.0.1:6379> XREVRANGE writers + - COUNT 1
33 | 1) 1) "1714701492187-0"
34 |    2) 1) "name"
35 |       2) "Ngozi"
36 |       3) "surname"
37 |       4) "Adichie"
38 | ```
39 |


--------------------------------------------------------------------------------
/commands/xsetid.md:
--------------------------------------------------------------------------------
1 | The `XSETID` command is an internal command.
2 | It is used by a Valkey primary to replicate the last delivered ID of streams.


--------------------------------------------------------------------------------
/commands/zcard.md:
--------------------------------------------------------------------------------
 1 | Returns the sorted set cardinality (number of elements) of the sorted set stored
 2 | at `key`.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> ZADD myzset 1 "one"
 8 | (integer) 1
 9 | 127.0.0.1:6379> ZADD myzset 2 "two"
10 | (integer) 1
11 | 127.0.0.1:6379> ZCARD myzset
12 | (integer) 2
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/zcount.md:
--------------------------------------------------------------------------------
 1 | Returns the number of elements in the sorted set at `key` with a score between
 2 | `min` and `max`.
 3 |
 4 | The `min` and `max` arguments have the same semantic as described for
 5 | `ZRANGEBYSCORE`.
 6 |
 7 | Note: the command has a complexity of just O(log(N)) because it uses elements ranks (see `ZRANK`) to get an idea of the range. Because of this there is no need to do a work proportional to the size of the range.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> ZADD myzset 1 "one"
13 | (integer) 1
14 | 127.0.0.1:6379> ZADD myzset 2 "two"
15 | (integer) 1
16 | 127.0.0.1:6379> ZADD myzset 3 "three"
17 | (integer) 1
18 | 127.0.0.1:6379> ZCOUNT myzset -inf +inf
19 | (integer) 3
20 | 127.0.0.1:6379> ZCOUNT myzset (1 3
21 | (integer) 2
22 | ```
23 |


--------------------------------------------------------------------------------
/commands/zdiff.md:
--------------------------------------------------------------------------------
 1 | This command is similar to `ZDIFFSTORE`, but instead of storing the resulting
 2 | sorted set, it is returned to the client.
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> ZADD zset1 1 "one"
 8 | (integer) 1
 9 | 127.0.0.1:6379> ZADD zset1 2 "two"
10 | (integer) 1
11 | 127.0.0.1:6379> ZADD zset1 3 "three"
12 | (integer) 1
13 | 127.0.0.1:6379> ZADD zset2 1 "one"
14 | (integer) 1
15 | 127.0.0.1:6379> ZADD zset2 2 "two"
16 | (integer) 1
17 | 127.0.0.1:6379> ZDIFF 2 zset1 zset2
18 | 1) "three"
19 | 127.0.0.1:6379> ZDIFF 2 zset1 zset2 WITHSCORES
20 | 1) "three"
21 | 2) "3"
22 | ```
23 |


--------------------------------------------------------------------------------
/commands/zdiffstore.md:
--------------------------------------------------------------------------------
 1 | Computes the difference between the first and all successive input sorted sets
 2 | and stores the result in `destination`. The total number of input keys is
 3 | specified by `numkeys`.
 4 |
 5 | Keys that do not exist are considered to be empty sets.
 6 |
 7 | If `destination` already exists, it is overwritten.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> ZADD zset1 1 "one"
13 | (integer) 1
14 | 127.0.0.1:6379> ZADD zset1 2 "two"
15 | (integer) 1
16 | 127.0.0.1:6379> ZADD zset1 3 "three"
17 | (integer) 1
18 | 127.0.0.1:6379> ZADD zset2 1 "one"
19 | (integer) 1
20 | 127.0.0.1:6379> ZADD zset2 2 "two"
21 | (integer) 1
22 | 127.0.0.1:6379> ZDIFFSTORE out 2 zset1 zset2
23 | (integer) 1
24 | 127.0.0.1:6379> ZRANGE out 0 -1 WITHSCORES
25 | 1) "three"
26 | 2) "3"
27 | ```
28 |


--------------------------------------------------------------------------------
/commands/zincrby.md:
--------------------------------------------------------------------------------
 1 | Increments the score of `member` in the sorted set stored at `key` by
 2 | `increment`.
 3 | If `member` does not exist in the sorted set, it is added with `increment` as
 4 | its score (as if its previous score was `0.0`).
 5 | If `key` does not exist, a new sorted set with the specified `member` as its
 6 | sole member is created.
 7 |
 8 | An error is returned when `key` exists but does not hold a sorted set.
 9 |
10 | The `score` value should be the string representation of a numeric value, and
11 | accepts double precision floating point numbers.
12 | It is possible to provide a negative value to decrement the score.
13 |
14 | ## Examples
15 |
16 | ```
17 | 127.0.0.1:6379> ZADD myzset 1 "one"
18 | (integer) 1
19 | 127.0.0.1:6379> ZADD myzset 2 "two"
20 | (integer) 1
21 | 127.0.0.1:6379> ZINCRBY myzset 2 "one"
22 | "3"
23 | 127.0.0.1:6379> ZRANGE myzset 0 -1 WITHSCORES
24 | 1) "two"
25 | 2) "2"
26 | 3) "one"
27 | 4) "3"
28 | ```
29 |


--------------------------------------------------------------------------------
/commands/zinter.md:
--------------------------------------------------------------------------------
 1 | This command is similar to `ZINTERSTORE`, but instead of storing the resulting
 2 | sorted set, it is returned to the client.
 3 |
 4 | For a description of the `WEIGHTS` and `AGGREGATE` options, see `ZUNIONSTORE`.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> ZADD zset1 1 "one"
10 | (integer) 1
11 | 127.0.0.1:6379> ZADD zset1 2 "two"
12 | (integer) 1
13 | 127.0.0.1:6379> ZADD zset2 1 "one"
14 | (integer) 1
15 | 127.0.0.1:6379> ZADD zset2 2 "two"
16 | (integer) 1
17 | 127.0.0.1:6379> ZADD zset2 3 "three"
18 | (integer) 1
19 | 127.0.0.1:6379> ZINTER 2 zset1 zset2
20 | 1) "one"
21 | 2) "two"
22 | 127.0.0.1:6379> ZINTER 2 zset1 zset2 WITHSCORES
23 | 1) "one"
24 | 2) "2"
25 | 3) "two"
26 | 4) "4"
27 | ```
28 |


--------------------------------------------------------------------------------
/commands/zintercard.md:
--------------------------------------------------------------------------------
 1 | This command is similar to `ZINTER`, but instead of returning the result set, it returns just the cardinality of the result.
 2 |
 3 | Keys that do not exist are considered to be empty sets.
 4 | With one of the keys being an empty set, the resulting set is also empty (since set intersection with an empty set always results in an empty set).
 5 |
 6 | By default, the command calculates the cardinality of the intersection of all given sets.
 7 | When provided with the optional `LIMIT` argument (which defaults to 0 and means unlimited), if the intersection cardinality reaches limit partway through the computation, the algorithm will exit and yield limit as the cardinality.
 8 | Such implementation ensures a significant speedup for queries where the limit is lower than the actual intersection cardinality.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> ZADD zset1 1 "one"
14 | (integer) 1
15 | 127.0.0.1:6379> ZADD zset1 2 "two"
16 | (integer) 1
17 | 127.0.0.1:6379> ZADD zset2 1 "one"
18 | (integer) 1
19 | 127.0.0.1:6379> ZADD zset2 2 "two"
20 | (integer) 1
21 | 127.0.0.1:6379> ZADD zset2 3 "three"
22 | (integer) 1
23 | 127.0.0.1:6379> ZINTER 2 zset1 zset2
24 | 1) "one"
25 | 2) "two"
26 | 127.0.0.1:6379> ZINTERCARD 2 zset1 zset2
27 | (integer) 2
28 | 127.0.0.1:6379> ZINTERCARD 2 zset1 zset2 LIMIT 1
29 | (integer) 1
30 | ```
31 |


--------------------------------------------------------------------------------
/commands/zinterstore.md:
--------------------------------------------------------------------------------
 1 | Computes the intersection of `numkeys` sorted sets given by the specified keys,
 2 | and stores the result in `destination`.
 3 | It is mandatory to provide the number of input keys (`numkeys`) before passing
 4 | the input keys and the other (optional) arguments.
 5 |
 6 | By default, the resulting score of an element is the sum of its scores in the
 7 | sorted sets where it exists.
 8 | Because intersection requires an element to be a member of every given sorted
 9 | set, this results in the score of every element in the resulting sorted set to
10 | be equal to the number of input sorted sets.
11 |
12 | For a description of the `WEIGHTS` and `AGGREGATE` options, see `ZUNIONSTORE`.
13 |
14 | If `destination` already exists, it is overwritten.
15 |
16 | ## Examples
17 |
18 | ```
19 | 127.0.0.1:6379> ZADD zset1 1 "one"
20 | (integer) 1
21 | 127.0.0.1:6379> ZADD zset1 2 "two"
22 | (integer) 1
23 | 127.0.0.1:6379> ZADD zset2 1 "one"
24 | (integer) 1
25 | 127.0.0.1:6379> ZADD zset2 2 "two"
26 | (integer) 1
27 | 127.0.0.1:6379> ZADD zset2 3 "three"
28 | (integer) 1
29 | 127.0.0.1:6379> ZINTERSTORE out 2 zset1 zset2 WEIGHTS 2 3
30 | (integer) 2
31 | 127.0.0.1:6379> ZRANGE out 0 -1 WITHSCORES
32 | 1) "one"
33 | 2) "5"
34 | 3) "two"
35 | 4) "10"
36 | ```
37 |


--------------------------------------------------------------------------------
/commands/zlexcount.md:
--------------------------------------------------------------------------------
 1 | When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns the number of elements in the sorted set at `key` with a value between `min` and `max`.
 2 |
 3 | The `min` and `max` arguments have the same meaning as described for
 4 | `ZRANGEBYLEX`.
 5 |
 6 | Note: the command has a complexity of just O(log(N)) because it uses elements ranks (see `ZRANK`) to get an idea of the range. Because of this there is no need to do a work proportional to the size of the range.
 7 |
 8 | ## Examples
 9 |
10 | ```
11 | 127.0.0.1:6379> ZADD myzset 0 a 0 b 0 c 0 d 0 e
12 | (integer) 5
13 | 127.0.0.1:6379> ZADD myzset 0 f 0 g
14 | (integer) 2
15 | 127.0.0.1:6379> ZLEXCOUNT myzset - +
16 | (integer) 7
17 | 127.0.0.1:6379> ZLEXCOUNT myzset [b [f
18 | (integer) 5
19 | ```
20 |


--------------------------------------------------------------------------------
/commands/zmscore.md:
--------------------------------------------------------------------------------
 1 | Returns the scores associated with the specified `members` in the sorted set stored at `key`.
 2 |
 3 | For every `member` that does not exist in the sorted set, a `nil` value is returned.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> ZADD myzset 1 "one"
 9 | (integer) 1
10 | 127.0.0.1:6379> ZADD myzset 2 "two"
11 | (integer) 1
12 | 127.0.0.1:6379> ZMSCORE myzset "one" "two" "nofield"
13 | 1) "1"
14 | 2) "2"
15 | 3) (nil)
16 | ```
17 |


--------------------------------------------------------------------------------
/commands/zpopmax.md:
--------------------------------------------------------------------------------
 1 | Removes and returns up to `count` members with the highest scores in the sorted
 2 | set stored at `key`.
 3 |
 4 | When left unspecified, the default value for `count` is 1. Specifying a `count`
 5 | value that is higher than the sorted set's cardinality will not produce an
 6 | error. When returning multiple elements, the one with the highest score will
 7 | be the first, followed by the elements with lower scores.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> ZADD myzset 1 "one"
13 | (integer) 1
14 | 127.0.0.1:6379> ZADD myzset 2 "two"
15 | (integer) 1
16 | 127.0.0.1:6379> ZADD myzset 3 "three"
17 | (integer) 1
18 | 127.0.0.1:6379> ZPOPMAX myzset
19 | 1) "three"
20 | 2) "3"
21 | ```
22 |


--------------------------------------------------------------------------------
/commands/zpopmin.md:
--------------------------------------------------------------------------------
 1 | Removes and returns up to `count` members with the lowest scores in the sorted
 2 | set stored at `key`.
 3 |
 4 | When left unspecified, the default value for `count` is 1. Specifying a `count`
 5 | value that is higher than the sorted set's cardinality will not produce an
 6 | error. When returning multiple elements, the one with the lowest score will
 7 | be the first, followed by the elements with greater scores.
 8 |
 9 | ## Examples
10 |
11 | ```
12 | 127.0.0.1:6379> ZADD myzset 1 "one"
13 | (integer) 1
14 | 127.0.0.1:6379> ZADD myzset 2 "two"
15 | (integer) 1
16 | 127.0.0.1:6379> ZADD myzset 3 "three"
17 | (integer) 1
18 | 127.0.0.1:6379> ZPOPMIN myzset
19 | 1) "one"
20 | 2) "1"
21 | ```
22 |


--------------------------------------------------------------------------------
/commands/zrangestore.md:
--------------------------------------------------------------------------------
 1 | This command is like `ZRANGE`, but stores the result in the `<dst>` destination key.
 2 |
 3 | ## Examples
 4 |
 5 | ```
 6 | 127.0.0.1:6379> ZADD srczset 1 "one" 2 "two" 3 "three" 4 "four"
 7 | (integer) 4
 8 | 127.0.0.1:6379> ZRANGESTORE dstzset srczset 2 -1
 9 | (integer) 2
10 | 127.0.0.1:6379> ZRANGE dstzset 0 -1
11 | 1) "three"
12 | 2) "four"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/zrank.md:
--------------------------------------------------------------------------------
 1 | Returns the rank of `member` in the sorted set stored at `key`, with the scores
 2 | ordered from low to high.
 3 | The rank (or index) is 0-based, which means that the member with the lowest
 4 | score has rank `0`.
 5 |
 6 | The optional `WITHSCORE` argument supplements the command's reply with the score of the element returned.
 7 |
 8 | Use `ZREVRANK` to get the rank of an element with the scores ordered from high
 9 | to low.
10 |
11 | ## Examples
12 |
13 | ```
14 | 127.0.0.1:6379> ZADD myzset 1 "one"
15 | (integer) 1
16 | 127.0.0.1:6379> ZADD myzset 2 "two"
17 | (integer) 1
18 | 127.0.0.1:6379> ZADD myzset 3 "three"
19 | (integer) 1
20 | 127.0.0.1:6379> ZRANK myzset "three"
21 | (integer) 2
22 | 127.0.0.1:6379> ZRANK myzset "four"
23 | (nil)
24 | 127.0.0.1:6379> ZRANK myzset "three" WITHSCORE
25 | 1) (integer) 2
26 | 2) "3"
27 | 127.0.0.1:6379> ZRANK myzset "four" WITHSCORE
28 | (nil)
29 | ```
30 |


--------------------------------------------------------------------------------
/commands/zrem.md:
--------------------------------------------------------------------------------
 1 | Removes the specified members from the sorted set stored at `key`.
 2 | Non existing members are ignored.
 3 |
 4 | An error is returned when `key` exists and does not hold a sorted set.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> ZADD myzset 1 "one"
10 | (integer) 1
11 | 127.0.0.1:6379> ZADD myzset 2 "two"
12 | (integer) 1
13 | 127.0.0.1:6379> ZADD myzset 3 "three"
14 | (integer) 1
15 | 127.0.0.1:6379> ZREM myzset "two"
16 | (integer) 1
17 | 127.0.0.1:6379> ZRANGE myzset 0 -1 WITHSCORES
18 | 1) "one"
19 | 2) "1"
20 | 3) "three"
21 | 4) "3"
22 | ```
23 |


--------------------------------------------------------------------------------
/commands/zremrangebylex.md:
--------------------------------------------------------------------------------
 1 | When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command removes all elements in the sorted set stored at `key` between the lexicographical range specified by `min` and `max`.
 2 |
 3 | The meaning of `min` and `max` are the same of the `ZRANGEBYLEX` command. Similarly, this command actually removes the same elements that `ZRANGEBYLEX` would return if called with the same `min` and `max` arguments.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> ZADD myzset 0 aaaa 0 b 0 c 0 d 0 e
 9 | (integer) 5
10 | 127.0.0.1:6379> ZADD myzset 0 foo 0 zap 0 zip 0 ALPHA 0 alpha
11 | (integer) 5
12 | 127.0.0.1:6379> ZRANGE myzset 0 -1
13 |  1) "ALPHA"
14 |  2) "aaaa"
15 |  3) "alpha"
16 |  4) "b"
17 |  5) "c"
18 |  6) "d"
19 |  7) "e"
20 |  8) "foo"
21 |  9) "zap"
22 | 10) "zip"
23 | 127.0.0.1:6379> ZREMRANGEBYLEX myzset [alpha [omega
24 | (integer) 6
25 | 127.0.0.1:6379> ZRANGE myzset 0 -1
26 | 1) "ALPHA"
27 | 2) "aaaa"
28 | 3) "zap"
29 | 4) "zip"
30 | ```
31 |


--------------------------------------------------------------------------------
/commands/zremrangebyrank.md:
--------------------------------------------------------------------------------
 1 | Removes all elements in the sorted set stored at `key` with rank between `start`
 2 | and `stop`.
 3 | Both `start` and `stop` are `0` -based indexes with `0` being the element with
 4 | the lowest score.
 5 | These indexes can be negative numbers, where they indicate offsets starting at
 6 | the element with the highest score.
 7 | For example: `-1` is the element with the highest score, `-2` the element with
 8 | the second highest score and so forth.
 9 |
10 | ## Examples
11 |
12 | ```
13 | 127.0.0.1:6379> ZADD myzset 1 "one"
14 | (integer) 1
15 | 127.0.0.1:6379> ZADD myzset 2 "two"
16 | (integer) 1
17 | 127.0.0.1:6379> ZADD myzset 3 "three"
18 | (integer) 1
19 | 127.0.0.1:6379> ZREMRANGEBYRANK myzset 0 1
20 | (integer) 2
21 | 127.0.0.1:6379> ZRANGE myzset 0 -1 WITHSCORES
22 | 1) "three"
23 | 2) "3"
24 | ```
25 |


--------------------------------------------------------------------------------
/commands/zremrangebyscore.md:
--------------------------------------------------------------------------------
 1 | Removes all elements in the sorted set stored at `key` with a score between
 2 | `min` and `max` (inclusive).
 3 |
 4 | ## Examples
 5 |
 6 | ```
 7 | 127.0.0.1:6379> ZADD myzset 1 "one"
 8 | (integer) 1
 9 | 127.0.0.1:6379> ZADD myzset 2 "two"
10 | (integer) 1
11 | 127.0.0.1:6379> ZADD myzset 3 "three"
12 | (integer) 1
13 | 127.0.0.1:6379> ZREMRANGEBYSCORE myzset -inf (2
14 | (integer) 1
15 | 127.0.0.1:6379> ZRANGE myzset 0 -1 WITHSCORES
16 | 1) "two"
17 | 2) "2"
18 | 3) "three"
19 | 4) "3"
20 | ```
21 |


--------------------------------------------------------------------------------
/commands/zrevrange.md:
--------------------------------------------------------------------------------
 1 | Returns the specified range of elements in the sorted set stored at `key`.
 2 | The elements are considered to be ordered from the highest to the lowest score.
 3 | Descending lexicographical order is used for elements with equal score.
 4 |
 5 | Apart from the reversed ordering, `ZREVRANGE` is similar to `ZRANGE`.
 6 |
 7 | ## Examples
 8 |
 9 | ```
10 | 127.0.0.1:6379> ZADD myzset 1 "one"
11 | (integer) 1
12 | 127.0.0.1:6379> ZADD myzset 2 "two"
13 | (integer) 1
14 | 127.0.0.1:6379> ZADD myzset 3 "three"
15 | (integer) 1
16 | 127.0.0.1:6379> ZREVRANGE myzset 0 -1
17 | 1) "three"
18 | 2) "two"
19 | 3) "one"
20 | 127.0.0.1:6379> ZREVRANGE myzset 2 3
21 | 1) "one"
22 | 127.0.0.1:6379> ZREVRANGE myzset -2 -1
23 | 1) "two"
24 | 2) "one"
25 | ```
26 |


--------------------------------------------------------------------------------
/commands/zrevrangebylex.md:
--------------------------------------------------------------------------------
 1 | When all the elements in a sorted set are inserted with the same score, in order to force lexicographical ordering, this command returns all the elements in the sorted set at `key` with a value between `max` and `min`.
 2 |
 3 | Apart from the reversed ordering, `ZREVRANGEBYLEX` is similar to `ZRANGEBYLEX`.
 4 |
 5 | ## Examples
 6 |
 7 | ```
 8 | 127.0.0.1:6379> ZADD myzset 0 a 0 b 0 c 0 d 0 e 0 f 0 g
 9 | (integer) 7
10 | 127.0.0.1:6379> ZREVRANGEBYLEX myzset [c -
11 | 1) "c"
12 | 2) "b"
13 | 3) "a"
14 | 127.0.0.1:6379> ZREVRANGEBYLEX myzset (c -
15 | 1) "b"
16 | 2) "a"
17 | 127.0.0.1:6379> ZREVRANGEBYLEX myzset (g [aaa
18 | 1) "f"
19 | 2) "e"
20 | 3) "d"
21 | 4) "c"
22 | 5) "b"
23 | ```
24 |


--------------------------------------------------------------------------------
/commands/zrevrangebyscore.md:
--------------------------------------------------------------------------------
 1 | Returns all the elements in the sorted set at `key` with a score between `max`
 2 | and `min` (including elements with score equal to `max` or `min`).
 3 | In contrary to the default ordering of sorted sets, for this command the
 4 | elements are considered to be ordered from high to low scores.
 5 |
 6 | The elements having the same score are returned in reverse lexicographical
 7 | order.
 8 |
 9 | Apart from the reversed ordering, `ZREVRANGEBYSCORE` is similar to
10 | `ZRANGEBYSCORE`.
11 |
12 | ## Examples
13 |
14 | ```
15 | 127.0.0.1:6379> ZADD myzset 1 "one"
16 | (integer) 1
17 | 127.0.0.1:6379> ZADD myzset 2 "two"
18 | (integer) 1
19 | 127.0.0.1:6379> ZADD myzset 3 "three"
20 | (integer) 1
21 | 127.0.0.1:6379> ZREVRANGEBYSCORE myzset +inf -inf
22 | 1) "three"
23 | 2) "two"
24 | 3) "one"
25 | 127.0.0.1:6379> ZREVRANGEBYSCORE myzset 2 1
26 | 1) "two"
27 | 2) "one"
28 | 127.0.0.1:6379> ZREVRANGEBYSCORE myzset 2 (1
29 | 1) "two"
30 | 127.0.0.1:6379> ZREVRANGEBYSCORE myzset (2 (1
31 | (empty array)
32 | ```
33 |


--------------------------------------------------------------------------------
/commands/zrevrank.md:
--------------------------------------------------------------------------------
 1 | Returns the rank of `member` in the sorted set stored at `key`, with the scores
 2 | ordered from high to low.
 3 | The rank (or index) is 0-based, which means that the member with the highest
 4 | score has rank `0`.
 5 |
 6 | The optional `WITHSCORE` argument supplements the command's reply with the score of the element returned.
 7 |
 8 | Use `ZRANK` to get the rank of an element with the scores ordered from low to
 9 | high.
10 |
11 | ## Examples
12 |
13 | ```
14 | 127.0.0.1:6379> ZADD myzset 1 "one"
15 | (integer) 1
16 | 127.0.0.1:6379> ZADD myzset 2 "two"
17 | (integer) 1
18 | 127.0.0.1:6379> ZADD myzset 3 "three"
19 | (integer) 1
20 | 127.0.0.1:6379> ZREVRANK myzset "one"
21 | (integer) 2
22 | 127.0.0.1:6379> ZREVRANK myzset "four"
23 | (nil)
24 | 127.0.0.1:6379> ZREVRANK myzset "three" WITHSCORE
25 | 1) (integer) 0
26 | 2) "3"
27 | 127.0.0.1:6379> ZREVRANK myzset "four" WITHSCORE
28 | (nil)
29 | ```
30 |


--------------------------------------------------------------------------------
/commands/zscan.md:
--------------------------------------------------------------------------------
1 | See `SCAN` for `ZSCAN` documentation.
2 |


--------------------------------------------------------------------------------
/commands/zscore.md:
--------------------------------------------------------------------------------
 1 | Returns the score of `member` in the sorted set at `key`.
 2 |
 3 | If `member` does not exist in the sorted set, or `key` does not exist, `nil` is
 4 | returned.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> ZADD myzset 1 "one"
10 | (integer) 1
11 | 127.0.0.1:6379> ZSCORE myzset "one"
12 | "1"
13 | ```
14 |


--------------------------------------------------------------------------------
/commands/zunion.md:
--------------------------------------------------------------------------------
 1 | This command is similar to `ZUNIONSTORE`, but instead of storing the resulting
 2 | sorted set, it is returned to the client.
 3 |
 4 | For a description of the `WEIGHTS` and `AGGREGATE` options, see `ZUNIONSTORE`.
 5 |
 6 | ## Examples
 7 |
 8 | ```
 9 | 127.0.0.1:6379> ZADD zset1 1 "one"
10 | (integer) 1
11 | 127.0.0.1:6379> ZADD zset1 2 "two"
12 | (integer) 1
13 | 127.0.0.1:6379> ZADD zset2 1 "one"
14 | (integer) 1
15 | 127.0.0.1:6379> ZADD zset2 2 "two"
16 | (integer) 1
17 | 127.0.0.1:6379> ZADD zset2 3 "three"
18 | (integer) 1
19 | 127.0.0.1:6379> ZUNION 2 zset1 zset2
20 | 1) "one"
21 | 2) "three"
22 | 3) "two"
23 | 127.0.0.1:6379> ZUNION 2 zset1 zset2 WITHSCORES
24 | 1) "one"
25 | 2) "2"
26 | 3) "three"
27 | 4) "3"
28 | 5) "two"
29 | 6) "4"
30 | ```
31 |


--------------------------------------------------------------------------------
/resources/clients/index.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: "Clients"
 3 | linkTitle: "Clients"
 4 | weight: 10
 5 | description: Implementations of the Redis protocol in different programming languages. To get started with an official client, click on one of the quickstart guide links below.
 6 | layout: bazzar
 7 | bazzar: clients
 8 | aliases:
 9 |     - /resources/clients
10 |     - /resources/clients/
11 | ---
12 |
13 |


--------------------------------------------------------------------------------
/resources/libraries/index.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: "Libraries"
 3 | linkTitle: "Libraries"
 4 | weight: 11
 5 | description: Libraries that use Redis and can be used by applications
 6 | layout: bazzar
 7 | bazzar: libraries
 8 | aliases:
 9 |     - /docs/libraries/
10 | ---
11 |
12 |


--------------------------------------------------------------------------------
/resources/modules/index.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: "Modules"
 3 | linkTitle: "Modules"
 4 | weight: 13
 5 | description: Redis modules extend the server's functionality in various ways
 6 | layout: bazzar
 7 | bazzar: modules
 8 | aliases:
 9 |     - /modules
10 |     - /modules/
11 |     - /docs/modules/
12 | ---
13 |
14 |


--------------------------------------------------------------------------------
/resources/tools/index.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: "Tools"
 3 | linkTitle: "Tools"
 4 | weight: 12
 5 | description: Tools for managing and deploying Redis
 6 | layout: bazzar
 7 | bazzar: tools
 8 | aliases:
 9 |     - /docs/tools/
10 | ---
11 |
12 |


--------------------------------------------------------------------------------
/topics/geospatial.md:
--------------------------------------------------------------------------------
 1 | ﻿---
 2 | title: "Geospatial"
 3 | description: >
 4 |     Introduction to the Valkey Geospatial data type
 5 | ---
 6 |
 7 | Geospatial indexes let you store coordinates and search for them.
 8 | This data structure is useful for finding nearby points within a given radius or bounding box.
 9 |
10 | ## Basic commands
11 |
12 | * `GEOADD` adds a location to a given geospatial index (note that longitude comes before latitude with this command).
13 | * `GEOSEARCH` returns locations with a given radius or a bounding box.
14 |
15 | See the [complete list of geospatial index commands](../commands/#geo).
16 |
17 |
18 | ## Examples
19 |
20 | Suppose you're building a mobile app that lets you find all of the bike rental stations closest to your current location.
21 |
22 | Add several locations to a geospatial index:
23 | ```
24 | 127.0.0.1:6379> GEOADD bikes:rentable -122.27652 37.805186 station:1
25 | (integer) 1
26 | 127.0.0.1:6379> GEOADD bikes:rentable -122.2674626 37.8062344 station:2
27 | (integer) 1
28 | 127.0.0.1:6379> GEOADD bikes:rentable -122.2469854 37.8104049 station:3
29 | (integer) 1
30 | ```
31 |
32 | Find all locations within a 5 kilometer radius of a given location, and return the distance to each location:
33 | ```
34 | 127.0.0.1:6379> GEOSEARCH bikes:rentable FROMLONLAT -122.2612767 37.7936847 BYRADIUS 5 km WITHDIST
35 | 1) 1) "station:1"
36 |    2) "1.8523"
37 | 2) 1) "station:2"
38 |    2) "1.4979"
39 | 3) 1) "station:3"
40 |    2) "2.2441"
41 | ```
42 |


--------------------------------------------------------------------------------
/topics/problems.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | title: "Troubleshooting Valkey"
 3 | description: Problems with Valkey? Start here.
 4 | ---
 5 |
 6 | This page tries to help you with what to do if you have issues with Valkey. Part of the Valkey project is helping people that are experiencing problems because we don't like to leave people alone with their issues.
 7 |
 8 | * If you have **latency problems** with Valkey, that in some way appears to be idle for some time, read our [Valkey latency troubleshooting guide](latency.md).
 9 | * Valkey stable releases are usually very reliable, however in the rare event you are **experiencing crashes** the developers can help a lot more if you provide debugging information. Please read our [Debugging Valkey guide](debugging.md).
10 | * We have a long history of users experiencing crashes with Valkey that actually turned out to be servers with **broken RAM**. Please test your RAM using **valkey-server --test-memory** in case Valkey is not stable in your system. Valkey built-in memory test is fast and reasonably reliable, but if you can you should reboot your server and use [memtest86](https://memtest86.com).
11 |


--------------------------------------------------------------------------------

├── README.md
├── src
    └── rapidjson
    │   └── README.md
└── tst
    └── integration
        └── README.md


/README.md:
--------------------------------------------------------------------------------
  1 | # Valkey JSON
  2 |
  3 | Valkey-json is a Valkey module written in C++ that provides native JSON (JavaScript Object Notation) support for Valkey. The implementation complies with RFC7159 and ECMA-404 JSON data interchange standards. Users can natively store, query, and modify JSON data structures using the JSONPath query language. The query expressions support advanced capabilities including wildcard selections, filter expressions, array slices, union operations, and recursive searches.
  4 |
  5 | Valkey-json leverages [RapidJSON](https://rapidjson.org/), a high-performance JSON parser and generator for C++, chosen for its small footprint and exceptional performance and memory efficiency. As a header-only library with no external dependencies, RapidJSON provides robust Unicode support while maintaining a compact memory profile of just 16 bytes per JSON value on most 32/64-bit machines.
  6 |
  7 | ## Building and Testing
  8 |
  9 | #### To build the module and run tests
 10 | ```text
 11 | # Build valkey-server (unstable) and run integration tests
 12 | ./build.sh
 13 | ```
 14 |
 15 | The default valkey version is "unstable". To override it, do:
 16 | ```text
 17 | # Build valkey-server (8.0) and run integration tests
 18 | SERVER_VERSION=8.0 ./build.sh
 19 | ```
 20 |
 21 | Custom compiler flags can be passed to the build script via environment variable CFLAGS. For example:
 22 | ```text
 23 | CFLAGS="-O0 -Wno-unused-function" ./build.sh
 24 | ```
 25 | #### To build the module with ASAN and run tests
 26 | ```text
 27 | export ASAN_BUILD=true
 28 | ./build.sh
 29 | ```
 30 |
 31 | #### To build just the module
 32 | ```text
 33 | mkdir build
 34 | cd build
 35 | cmake ..
 36 | make
 37 | ```
 38 |
 39 | The default valkey version is "unstable". To override it, do:
 40 | ```text
 41 | mkdir build
 42 | cd build
 43 | cmake .. -DVALKEY_VERSION=8.0
 44 | make
 45 | ```
 46 |
 47 | Custom compiler flags can be passed to cmake via variable CFLAGS. For example:
 48 | ```text
 49 | mkdir build
 50 | cd build
 51 | cmake .. -DCFLAGS="-O0 -Wno-unused-function"
 52 | make
 53 | ```
 54 |
 55 | #### To run all unit tests:
 56 | ```text
 57 | cd build
 58 | make -j unit
 59 | ```
 60 |
 61 | #### To run all integration tests:
 62 | ```text
 63 | make -j test
 64 | ```
 65 |
 66 | #### To run one integration test:
 67 | ```text
 68 | TEST_PATTERN=<test-function-or-file> make -j test
 69 | ```
 70 | e.g.,
 71 | ```text
 72 | TEST_PATTERN=test_sanity make -j test
 73 | TEST_PATTERN=test_rdb.py make -j test
 74 | ```
 75 |
 76 | ## Load the Module
 77 | To test the module with a Valkey, you can load the module using any of the following ways:
 78 |
 79 | #### Using valkey.conf:
 80 | ```
 81 | 1. Add the following to valkey.conf:
 82 |     loadmodule /path/to/libjson.so
 83 | 2. Start valkey-server:
 84 |     valkey-server /path/to/valkey.conf
 85 | ```
 86 |
 87 | #### Starting valkey with --loadmodule option:
 88 | ```text
 89 | valkey-server --loadmodule /path/to/libjson.so
 90 | ```
 91 |
 92 | #### Using Valkey command MODULE LOAD:
 93 | ```
 94 | 1. Connect to a running Valkey instance using valkey-cli
 95 | 2. Execute Valkey command:
 96 |     MODULE LOAD /path/to/libjson.so
 97 | ```
 98 | ## Supported  Module Commands
 99 | ```text
100 | JSON.ARRAPPEND
101 | JSON.ARRINDEX
102 | JSON.ARRINSERT
103 | JSON.ARRLEN
104 | JSON.ARRPOP
105 | JSON.ARRTRIM
106 | JSON.CLEAR
107 | JSON.DEBUG
108 | JSON.DEL
109 | JSON.FORGET
110 | JSON.GET
111 | JSON.MGET
112 | JSON.MSET
113 | JSON.NUMINCRBY
114 | JSON.NUMMULTBY
115 | JSON.OBJKEYS
116 | JSON.OBJLEN
117 | JSON.RESP
118 | JSON.SET
119 | JSON.STRAPPEND
120 | JSON.STRLEN
121 | JSON.TOGGLE
122 | JSON.TYPE
123 | ```
124 |


--------------------------------------------------------------------------------
/src/rapidjson/README.md:
--------------------------------------------------------------------------------
 1 | # RapidJSON Source Code
 2 | * The original RapidJSON Source Code is cloned at build time using CMAKELISTS
 3 | * Last commit on the master branch: ebd87cb468fb4cb060b37e579718c4a4125416c1, 2024-12-02
 4 |
 5 | # Modifications
 6 | We made a few changes to the RapidJSON source code. Before the changes are pushed to the open source,
 7 | we have to include a private copy of the file. Modified RapidJSON code is under src/rapidjson.
 8 |
 9 | ## document.h`
10 | We need to modify RapidJSON's document.h to support JSON depth limit.
11 |
12 | ### reader.h
13 | Modified reader.h to only generate integers in int64 range.
14 |
15 |


--------------------------------------------------------------------------------
/tst/integration/README.md:
--------------------------------------------------------------------------------
 1 | # Integration Tests
 2 |
 3 | This directory contains integration tests that verify the interaction between vlkaye-server and valkey-json module features working together. Unlike unit tests that test individual components in isolation, these tests validate the system's behavior as a whole.
 4 |
 5 | ## Requirements
 6 |
 7 | ```text
 8 | python 3.9
 9 | pytest 4
10 | ```


--------------------------------------------------------------------------------

├── QUICK_START.md
└── README.md


/QUICK_START.md:
--------------------------------------------------------------------------------
 1 | # Quick Start
 2 |
 3 | Follow these steps to set up, build, and run the Valkey server with the valkey-bloom module. This guide will walk you through creating a bloom filter, inserting items, and checking for items in the filters.
 4 |
 5 | ## Step 1: Install Valkey and valkey-bloom
 6 |
 7 | 1. Build Valkey from source by following the instructions [here](https://github.com/valkey-io/valkey?tab=readme-ov-file#building-valkey-using-makefile). Make sure to use Valkey version 8.0 or above.
 8 |
 9 | 2. Build the valkey-bloom module from source by following the instructions [here](https://github.com/valkey-io/valkey-bloom/blob/unstable/README.md#build-instructions).
10 |
11 | ## Step 2: Run the Valkey Server with valkey-bloom
12 |
13 | Once valkey-bloom is built, run the Valkey server with the module loaded:
14 |
15 | In case of Linux:
16 | ```bash
17 | ./valkey-server --loadmodule ./target/release/libvalkey_bloom.so
18 | ```
19 |
20 | You should see the Valkey server start, and it will be ready to accept commands.
21 |
22 | ## Step 3: Create a Bloom Filter
23 |
24 | Start a Valkey CLI session:
25 |
26 | ```bash
27 | valkey-cli
28 | ```
29 |
30 | Create a bloom filter using the BF.ADD, BF.INSERT, BF.RESERVE or BF.MADD commands. For example:
31 |
32 | ```bash
33 | BF.ADD filter-key item-val
34 | ```
35 |
36 | - `filter-key` is the name of the bloom filter we will be operating on
37 | - `item-val` is the item we are inserting into the bloom filter
38 |
39 | ## Step 4: Insert some more items
40 |
41 | To insert items on an already created filter, use the `BF.ADD`, `BF.MADD` or `BF.INSERT` commands:
42 |
43 | ```bash
44 | BF.ADD filter-key example
45 | BF.MADD filter-key example1 example2
46 | ```
47 |
48 | Replace the example with the actual items you want to add.
49 |
50 | ## Step 5: Check if items are present
51 |
52 | Now that you've created a bloom filter and inserted items, you can check what items have been added. Use the `BF.EXISTS` or `BF.MEXISTS` commands to check for items:
53 |
54 | ```bash
55 | BF.EXISTS filter-key example
56 | ```
57 |
58 | This command checks if an item is present in a bloom filter. Bloom filters can have false positives, but no false negatives. This means that if the BF.EXISTS command returns 0, then the item is not present. But if the BF.EXISTS command returns 1, there is a possibility (determined by false positive rate) that the item is not actually present.
59 |


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
 1 | # valkey-bloom
 2 |
 3 | Valkey-Bloom (BSD-3-Clause) is a Rust based Valkey-Module which brings a Bloom Filter (Module) data type into Valkey and supports verions >= 8.0. With this, users can create bloom filters (space efficient probabilistic data structures) to add elements, check whether elements exists, auto scale their filters, customize bloom filter properties, perform RDB Save and load operations, etc.
 4 |
 5 | Valkey-Bloom is built using `bloomfilter::Bloom` (https://crates.io/crates/bloomfilter which has a BSD-2-Clause license).
 6 |
 7 | It is API compatible with the bloom filter command syntax of the official Valkey client libraries including valkey-py, valkey-java, valkey-go (as well as the equivalent Redis libraries)
 8 |
 9 | ## Supported commands
10 | ```
11 | BF.EXISTS
12 | BF.ADD
13 | BF.MEXISTS
14 | BF.MADD
15 | BF.CARD
16 | BF.RESERVE
17 | BF.INFO
18 | BF.INSERT
19 | BF.LOAD
20 | ```
21 |
22 | ## Build instructions
23 | ```
24 | curl https://sh.rustup.rs -sSf | sh
25 | sudo yum install clang
26 | git clone https://github.com/valkey-io/valkey-bloom.git
27 | cd valkey-bloom
28 | # Building for Valkey 8.1 and above:
29 | cargo build --release
30 | # Building for Valkey 8.0 specifically:
31 | cargo build --release --features valkey_8_0
32 | valkey-server --loadmodule ./target/release/libvalkey_bloom.so
33 | ```
34 |
35 | #### Local development script to build, run format checks, run unit / integration tests, and for cargo release:
36 | ```
37 | # Builds the valkey-server (unstable) for integration testing.
38 | SERVER_VERSION=unstable
39 | ./build.sh
40 | # Same as above, but uses valkey-server (8.0.0) for integration testing.
41 | SERVER_VERSION=8.0.0
42 | ./build.sh
43 | # Build with asan, you may need to remove the old valkey binary if you have used ./build.sh before. You can do this by deleting the `.build` folder in the `tests` folder
44 | ASAN_BUILD=true
45 | ./build.sh
46 | ```
47 |
48 | ## Load the Module
49 | To test the module with a Valkey, you can load the module in the following ways:
50 |
51 | #### Using valkey.conf:
52 | ```
53 | 1. Add the following to valkey.conf:
54 |     loadmodule /path/to/libvalkey_bloom.so
55 | 2. Start valkey-server:
56 |     valkey-server /path/to/valkey.conf
57 | ```
58 |
59 | #### Starting Valkey with the `--loadmodule` option:
60 | ```text
61 | valkey-server --loadmodule /path/to/libvalkey_bloom.so
62 | ```
63 |
64 | #### Using the Valkey command `MODULE LOAD`:
65 | ```
66 | 1. Connect to a running Valkey instance using valkey-cli
67 | 2. Execute Valkey command:
68 |     MODULE LOAD /path/to/libvalkey_bloom.so
69 | ```
70 | ## Feature Flags
71 |
72 | * valkey_8_0: valkey-bloom is intended to be loaded on server versions >= Valkey 8.1 and by default it is built this way (unless this flag is provided). It is however compatible with Valkey version 8.0 if the user explicitly provides this feature flag in their cargo build command.
73 | ```
74 | cargo build --release --features valkey_8_0
75 | ```
76 |
77 | This can also be done by specifiyng SERVER_VERSION=8.0.0 and then running `./build.sh`


--------------------------------------------------------------------------------

├── COMMANDS.md
├── QUICK_START.md
├── README.md
├── rfc
    └── TEMPLATE.md
├── third_party
    └── hdrhistogram_c
    │   └── README.md
└── vmsdk
    └── README.md


/COMMANDS.md:
--------------------------------------------------------------------------------
  1 | # Command List
  2 | - [`FT.CREATE`](#ftcreate)
  3 | - [`FT.DROPINDEX`](#ftdropindex)
  4 | - [`FT.INFO`](#ftinfo)
  5 | - [`FT._LIST`](#ft_list)
  6 | - [`FT.SEARCH`](#ftsearch)
  7 | #
  8 |
  9 | ## FT.CREATE
 10 |
 11 | The `FT.CREATE` command creates an empty index and initiates the backfill process. Each index consists of a number of field definitions. Each field definition specifies a field name, a field type and a path within each indexed key to locate a value of the declared type. Some field type definitions have additional sub-type specifiers.
 12 |
 13 | For indexes on HASH keys, the path is the same as the hash member name. The optional `AS` clause can be used to rename the field if desired.
 14 | Renaming of fields is especially useful when the member name contains special characters.
 15 |
 16 | For indexes on JSON keys, the path is a JSON path to the data of the declared type. Because the JSON path always contains special characters, the `AS` clause is required.
 17 |
 18 |
 19 | ```bash
 20 | FT.CREATE <index-name>
 21 |     ON HASH
 22 |     [PREFIX <count> <prefix> [<prefix>...]]
 23 |     SCHEMA
 24 |         (
 25 |             <field-identifier> [AS <field-alias>]
 26 |                   NUMERIC
 27 |                 | TAG [SEPARATOR <sep>] [CASESENSITIVE]
 28 |                 | VECTOR [HNSW | FLAT] <attr_count> [<attribute_name> <attribute_value>]+)
 29 |         )+
 30 | ```
 31 |
 32 |
 33 | - **\<index-name\>** (required): This is the name you give to your index. If an index with the same name exists already, an error is returned.
 34 |
 35 | - **ON HASH | JSON** (optional): Only keys that match the specified type are included into this index. If omitted, HASH is assumed.
 36 |
 37 | - **PREFIX \<prefix-count\> \<prefix\>** (optional): If this clause is specified, then only keys that begin with the same bytes as one or more of the specified prefixes will be included into this index. If this clause is omitted, all keys of the correct type will be included. A zero-length prefix would also match all keys of the correct type.
 38 |
 39 | ### Field types
 40 |
 41 | **TAG**: A tag field is a string that contains one or more tag values.
 42 |
 43 | - **SEPARATOR \<sep\>** (optional): One of these characters `,.<>{}[]"':;!@#$%^&*()-+=~` used to delimit individual tags. If omitted the default value is `,`.
 44 | - **CASESENSITIVE** (optional): If present, tag comparisons will be case sensitive. The default is that tag comparisons are NOT case sensitive
 45 |
 46 | **NUMERIC**: A numeric field contains a number.
 47 |
 48 | **VECTOR**: A vector field contains a vector. Two vector indexing algorithms are currently supported: HNSW (Hierarchical Navigable Small World) and FLAT (brute force). Each algorithm has a set of additional attributes, some required and other optional.
 49 |
 50 | - **FLAT:** The Flat algorithm provides exact answers, but has runtime proportional to the number of indexed vectors and thus may not be appropriate for large data sets.
 51 |   - **DIM \<number\>** (required): Specifies the number of dimensions in a vector.
 52 |   - **TYPE FLOAT32** (required): Data type, currently only FLOAT32 is supported.
 53 |   - **DISTANCE\_METRIC \[L2 | IP | COSINE\]** (required): Specifies the distance algorithm
 54 |   - **INITIAL\_CAP \<size\>** (optional): Initial index size.
 55 | - **HNSW:** The HNSW algorithm provides approximate answers, but operates substantially faster than FLAT.
 56 |   - **DIM \<number\>** (required): Specifies the number of dimensions in a vector.
 57 |   - **TYPE FLOAT32** (required): Data type, currently only FLOAT32 is supported.
 58 |   - **DISTANCE\_METRIC \[L2 | IP | COSINE\]** (required): Specifies the distance algorithm
 59 |   - **INITIAL\_CAP \<size\>** (optional): Initial index size.
 60 |   - **M \<number\>** (optional): Number of maximum allowed outgoing edges for each node in the graph in each layer. on layer zero the maximal number of outgoing edges will be 2\*M. Default is 16, the maximum is 512\.
 61 |   - **EF\_CONSTRUCTION \<number\>** (optional): controls the number of vectors examined during index construction. Higher values for this parameter will improve recall ratio at the expense of longer index creation times. The default value is 200\. Maximum value is 4096\.
 62 |   - **EF\_RUNTIME \<number\>** (optional):  controls  the number of vectors to be examined during a query operation. The default is 10, and the max is 4096\. You can set this parameter value for each query you run. Higher values increase query times, but improve query recall.
 63 |
 64 | **RESPONSE** OK or error.
 65 |
 66 | ## FT.DROPINDEX
 67 | ```
 68 | FT.DROPINDEX <index-name>
 69 | ```
 70 |
 71 | The specified index is deleted. It is an error if that index doesn't exist.
 72 |
 73 | - **\<index-name\>** (required): The name of the index to delete.
 74 |
 75 | **RESPONSE** OK or error.
 76 |
 77 | ## FT.INFO
 78 | ```
 79 | FT.INFO <index-name>
 80 | ```
 81 |
 82 | Detailed information about the specified index is returned.
 83 |
 84 | - **\<index-name\>** (required): The name of the index to return information about.
 85 |
 86 | **RESPONSE**
 87 |
 88 | An array of key value pairs.
 89 |
 90 | - **index\_name**	(string)	The index name
 91 | - **num\_docs**	(integer)	Total keys in the index
 92 | - **num\_records**	(integer)	Total records in the index
 93 | - **hash\_indexing\_failures**	(integer)	Count of unsuccessful indexing attempts
 94 | - **indexing**	(integer)	Binary value. Shows if background indexing is running or not
 95 | - **percent\_indexed**	(integer)	Progress of background indexing. Percentage is expressed as a value from 0 to 1
 96 | - **index\_definition**	(array)	An array of values defining the index
 97 |   - **key\_type**	(string)	HASH. This is the only available key type.
 98 |   - **prefixes**	(array of strings)	Prefixes for keys
 99 |   - **default\_score**	(integer) This is the default scoring value for the vector search scoring function, which is used for sorting.
100 |   - **attributes**	(array)	One array of entries for each field defined in the index.
101 |     - **identifier**	(string)	field name
102 |     - **attribute**	(string)	An index field. This is correlated to a specific index HASH field.
103 |     - **type**	(string)	VECTOR. This is the only available type.
104 |     - **index**	(array)	Extended information about this internal index for this field.
105 |       - **capacity**	(integer)	The current capacity for the total number of vectors that the index can store.
106 |       - **dimensions**	(integer)	Dimension count
107 |       - **distance\_metric**	(string)	Possible values are L2, IP or Cosine
108 |       - **data\_type**	(string)	FLOAT32. This is the only available data type
109 |       - **algorithm**	(array)	Information about the algorithm for this field.
110 |         - **name**	(string)	HNSW or FLAT
111 |         - **m**	(integer)	The count of maximum permitted outgoing edges for each node in the graph in each layer. The maximum number of outgoing edges is 2\*M for layer 0\. The Default is 16\. The maximum is 512\.
112 |         - **ef\_construction**	(integer)	The count of vectors in the index. The default is 200, and the max is 4096\. Higher values increase the time needed to create indexes, but improve the recall ratio.
113 |         - **ef\_runtime**	(integer)	The count of vectors to be examined during a query operation. The default is 10, and the max is 4096\.
114 |
115 | ## FT._LIST
116 | ```
117 | FT._LIST
118 | ```
119 |
120 | Lists the currently defined indexes.
121 |
122 | **RESPONSE**
123 |
124 | An array of strings which are the currently defined index names.
125 |
126 | ## FT.SEARCH
127 | ```
128 | FT.SEARCH <index> <query>
129 |   [NOCONTENT]
130 |   [TIMEOUT <timeout>]
131 |   [PARAMS nargs <name> <value> [ <name> <value> ...]]
132 |   [LIMIT <offset> <num>]
133 |   [DIALECT <dialect>]
134 | ```
135 |
136 | Performs a search of the specified index. The keys which match the query expression are returned.
137 |
138 | - **\<index\>** (required): This index name you want to query.
139 | - **\<query\>** (required): The query string, see below for details.
140 | - **NOCONTENT** (optional): When present, only the resulting key names are returned, no key values are included.
141 | - **TIMEOUT \<timeout\>** (optional): Lets you set a timeout value for the search command. This must be an integer in milliSeconds.
142 | - **PARAMS \<count\> \<name1\> \<value1\> \<name2\> \<value2\> ...** (optional): `count` is of the number of arguments, i.e., twice the number of value name pairs. See the query string for usage details.
143 | - **RETURN \<count\> \<field1\> \<field2\> ...** (options): `count` is the number of fields to return. Specifies the fields you want to retrieve from your documents, along with any aliases for the returned values. By default, all fields are returned unless the NOCONTENT option is set, in which case no fields are returned. If num is set to 0, it behaves the same as NOCONTENT.
144 | - **LIMIT \<offset\> \<count\>** (optional): Lets you choose a portion of the result. The first `<offset>` keys are skipped and only a maximum of `<count>` keys are included. The default is LIMIT 0 10, which returns at most 10 keys.
145 | - **DIALECT \<dialect\>** (optional): Specifies your dialect. The only supported dialect is 2\.
146 |
147 | **RESPONSE**
148 |
149 | The command returns either an array if successful or an error.
150 |
151 | On success, the first entry in the response array represents the count of matching keys, followed by one array entry for each matching key.
152 | Note that if  the `LIMIT` option is specified it will only control the number of returned keys and will not affect the value of the first entry.
153 |
154 | When `NOCONTENT` is specified, each entry in the response contains only the matching keyname, Otherwise, each entry includes the matching keyname, followed by an array of the returned fields.
155 |
156 | The result fields for a key consists of a set of name/value pairs. The first name/value pair is for the distance computed. The name of this pair is constructed from the vector field name prepended with "\_\_" and appended with "\_score" and the value is the computed distance. The remaining name/value pairs are the members and values of the key as controlled by the `RETURN` clause.
157 |
158 | The query string conforms to this syntax:
159 |
160 | ```
161 | <filtering>=>[ KNN <K> @<vector_field_name>
lt;vector_parameter_name> <query-modifiers> ]
162 | ```
163 |
164 | Where:
165 |
166 | - **\<filtering\>** Is either a `*` or a filter expression. A `*` indicates no filtering and thus all vectors within the index are searched. A filter expression can be provided to designate a subset of the vectors to be searched.
167 | - **\<vector\_field\_name\>** The name of a vector field within the specified index.
168 | - **\<K\>** The number of nearest neighbor vectors to return.
169 | - **\<vector\_parameter\_name\>** A PARAM name whose corresponding value provides the query vector for the KNN algorithm. Note that this parameter must be encoded as a 32-bit IEEE 754 binary floating point in little-endian format.
170 | - **\<query-modifiers\>** (Optional) A list of keyword/value pairs that modify this particular KNN search. Currently two keywords are supported:
171 |   - **EF_RUNTIME** This keyword is accompanied by an integer value which overrides the default value of **EF_RUNTIME** specified when the index was created.
172 |   - **AS** This keyword is accompanied by a string value which becomes the name of the score field in the result, overriding the default score field name generation algorithm.
173 |
174 | **Filter Expression**
175 |
176 | A filter expression is constructed as a logical combination of Tag and Numeric search operators contained within parenthesis.
177 |
178 | **Tag**
179 |
180 | The tag search operator is specified with one or more strings separated by the `|` character. A key will satisfy the Tag search operator if the indicated field contains any one of the specified strings.
181 |
182 | ```
183 | @<field_name>:{<tag>}
184 | or
185 | @<field_name>:{<tag1> | <tag2>}
186 | or
187 | @<field_name>:{<tag1> | <tag2> | ...}
188 | ```
189 |
190 | For example, the following query will return documents with blue OR black OR green color.
191 |
192 | `@color:{blue | black | green}`
193 |
194 | As another example, the following query will return documents containing "hello world" or "hello universe"
195 |
196 | `@color:{hello world | hello universe}`
197 |
198 | **Numeric Range**
199 |
200 | Numeric range operator allows for filtering queries to only return values that are in between a given start and end value. Both inclusive and exclusive range queries are supported. For simple relational comparisons, \+inf, \-inf can be used with a range query.
201 |
202 | The syntax for a range search operator is:
203 |
204 | ```
205 | @<field_name>:[ [(] <bound> [(] <bound>]
206 | ```
207 |
208 | where \<bound\> is either a number or \+inf or \-inf
209 |
210 | Bounds without a leading open paren are inclusive, whereas bounds with the leading open paren are exclusive.
211 |
212 | Use the following table as a guide for mapping mathematical expressions to filtering queries:
213 |
214 | ```
215 | min <= field <= max         @field:[min max]
216 | min < field <= max          @field:[(min max]
217 | min <= field < max	        @field:[min (max]
218 | min < field < max	        @field:[(min (max]
219 | field >= min	            @field:[min +inf]
220 | field > min	                @field:[(min +inf]
221 | field <= max	            @field:[-inf max]
222 | field < max	                @field:[-inf (max]
223 | field == val	            @field:[val val]
224 | ```
225 |
226 | **Logical Operators**
227 |
228 | Multiple tags and numeric search operators can be used to construct complex queries using logical operators.
229 |
230 | **Logical AND**
231 |
232 | To set a logical AND, use a space between the predicates. For example:
233 |
234 | ```
235 | query1 query2 query3
236 | ```
237 |
238 | **Logical OR**
239 |
240 | To set a logical OR, use the `|` character between the predicates. For example:
241 |
242 | ```
243 | query1 | query2 | query3
244 | ```
245 |
246 | **Logical Negation**
247 |
248 | Any query can be negated by prepending the `-` character before each query. Negative queries return all entries that don't match the query. This also includes keys that don't have the field.
249 |
250 | For example, a negative query on @genre:{comedy} will return all books that are not comedy AND all books that don't have a genre field.
251 |
252 | The following query will return all books with "comedy" genre that are not published between 2015 and 2024, or that have no year field:
253 |
254 | @genre:\[comedy\] \-@year:\[2015 2024\]
255 |
256 | **Operator Precedence**
257 |
258 | Typical operator precedence rules apply, i.e., Logical negate is the highest priority, followed by Logical and and then Logical Or with the lowest priority. Parenthesis can be used to override the default precedence rules.
259 |
260 | **Examples of Combining Logical Operators**
261 |
262 | Logical operators can be combined to form complex filter expressions.
263 |
264 | The following query will return all books with "comedy" or "horror" genre (AND) published between 2015 and 2024:
265 |
266 | `@genre:[comedy|horror] @year:[2015 2024]`
267 |
268 | The following query will return all books with "comedy" or "horror" genre (OR) published between 2015 and 2024:
269 |
270 | `@genre:[comedy|horror] | @year:[2015 2024]`
271 |
272 | The following query will return all books that either don't have a genre field, or have a genre field not equal to "comedy", that are published between 2015 and 2024:
273 |
274 | `-@genre:[comedy] @year:[2015 2024]`
275 |


--------------------------------------------------------------------------------
/QUICK_START.md:
--------------------------------------------------------------------------------
 1 | # Quick Start
 2 |
 3 | Follow these steps to set up, build, and run the Valkey server with vector search capabilities. This guide will walk you through creating a vector index, inserting vectors, and issuing queries.
 4 |
 5 | ## Step 1: Install Valkey and valkey-search
 6 |
 7 | 1. Build Valkey from source by following the instructions [here](https://github.com/valkey-io/valkey?tab=readme-ov-file#building-valkey-using-makefile). Make sure to use Valkey version 7.2.6 or later as the previous versions have Valkey module API bugs.
 8 | 2. Build valkey-search module from source by following the instructions [here](https://github.com/valkey-io/valkey-search/tree/main?tab=readme-ov-file#build-instructions).
 9 |
10 | ## Step 2: Run the Valkey Server
11 |
12 | Once valkey-search is built, run the Valkey server with the valkey-search module loaded:
13 |
14 | ```bash
15 | ./valkey-server "--loadmodule libsearch.so  --reader-threads 64 --writer-threads 64"
16 | ```
17 |
18 | You should see the Valkey server start, and it will be ready to accept commands.
19 |
20 | ## Step 3: Create a Vector Index
21 |
22 | To enable vector search functionality, you need to create an index for storing vector data.
23 | Start a Valkey CLI session:
24 |
25 | ```bash
26 | valkey-cli
27 | ```
28 |
29 | Create a vector field using the FT.CREATE command. For example:
30 |
31 | ```bash
32 | FT.CREATE myIndex SCHEMA vector VECTOR HNSW 6 TYPE FLOAT32 DIM 3 DISTANCE_METRIC COSINE
33 | ```
34 |
35 | - `vector` is the vector field for storing the vectors.
36 | - `VECTOR HNSW` specifies the use of the HNSW (Hierarchical Navigable Small World) algorithm for vector search.
37 | - `DIM 3` sets the vector dimensionality to 3.
38 | - `DISTANCE_METRIC COSINE` sets the distance metric to cosine similarity.
39 |
40 | ## Step 4: Insert Some Vectors
41 |
42 | To insert vectors, use the `HSET` command:
43 |
44 | ```bash
45 | HSET my_hash_key_1 vector "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?"
46 | HSET my_hash_key_2 vector "\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x00\x80?"
47 | ```
48 |
49 | Replace the `\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?` and `\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x00\x80?` with actual vectors.
50 |
51 | ## Step 5: Issue Vector Queries
52 |
53 | Now that you've created an index and inserted vectors, you can perform a vector search. Use the `FT.SEARCH` command to find similar vectors:
54 |
55 | ```bash
56 | FT.SEARCH myIndex "*=>[KNN 5 @vector $query_vector]" PARAMS 2 query_vector "\xcd\xccL?\x00\x00\x00\x00\x00\x00\x00\x00"
57 | ```
58 |
59 | This command performs a K-nearest neighbors search and returns the top 5 closest vectors to the provided query vector.
60 |


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
  1 | # valkey-search
  2 |
  3 | **valkey-search** (BSD-3-Clause), provided as a Valkey module, is a high-performance Vector Similarity Search engine optimized for AI-driven workloads. It delivers single-digit millisecond latency and high QPS, capable of handling billions of vectors with over 99% recall.
  4 |
  5 | valkey-search allows users to create indexes and perform similarity searches, incorporating complex filters. It supports Approximate Nearest Neighbor (ANN) search with HNSW and exact matching using K-Nearest Neighbors (KNN). Users can index data using either **Valkey Hash** or **[Valkey-JSON](https://github.com/valkey-io/valkey-json)** data types.
  6 |
  7 | While valkey-search currently focuses on Vector Search, its goal is to extend Valkey into a full-fledged search engine, supporting Full Text Search and additional indexing options.
  8 |
  9 | ## Supported Commands
 10 |
 11 | ```plaintext
 12 | FT.CREATE
 13 | FT.DROPINDEX
 14 | FT.INFO
 15 | FT._LIST
 16 | FT.SEARCH
 17 | ```
 18 |
 19 | For a detailed description of the supported commands and configuration options, see the [Command Reference](https://github.com/valkey-io/valkey-search/blob/main/COMMANDS.md).
 20 |
 21 | For comprehensive examples, refer to the [Quick Start Guide](https://github.com/valkey-io/valkey-search/blob/main/QUICK_START.md).
 22 |
 23 | ## Scaling
 24 |
 25 | valkey-search supports both **Standalone** and **Cluster** modes. Query processing and ingestion scale linearly with CPU cores in both modes. For large storage requirements, users can leverage Cluster mode for horizontal scaling of the keyspace.
 26 |
 27 | If replica lag is acceptable, users can achieve horizontal query scaling by directing clients to read from replicas.
 28 |
 29 | ## Performance
 30 |
 31 | valkey-search achieves high performance by storing vectors in-memory and applying optimizations throughout the stack to efficiently utilize the host resources, such as:
 32 |
 33 | - **Parallelism:**  Threading model that enables lock-free execution in the read path.
 34 | - **CPU Cache Efficiency:** Designed to promote efficient use of CPU cache.
 35 | - **SIMD Optimizations:** Leveraging SIMD (Single Instruction, Multiple Data) for enhanced vector processing.
 36 |
 37 | ## Hybrid Queries
 38 |
 39 | valkey-search supports hybrid queries, combining Vector Similarity Search with filtering on indexed fields, such as **Numeric** and **Tag indexes**.
 40 |
 41 | There are two primary approaches to hybrid queries:
 42 |
 43 | - **Pre-filtering:** Begin by filtering the dataset and then perform an exact similarity search. This works well when the filtered result set is small but can be costly with larger datasets.
 44 | - **Post-filtering:** Perform the similarity search first, then filter the results. This is suitable when the filter-qualified result set is large but may lead to empty or lower than expected amount of results.
 45 |
 46 | valkey-search uses a **hybrid approach** with a query planner that selects the most efficient query execution path between:
 47 |
 48 | - **Pre-filtering**
 49 | - **Inline-filtering:** Filters results during the similarity search process.
 50 |
 51 | ## Build Instructions
 52 |
 53 | ### Install basic tools
 54 |
 55 | #### Ubuntu / Debian
 56 |
 57 | ```sh
 58 | sudo apt update
 59 | sudo apt install -y clangd          \
 60 |                     build-essential \
 61 |                     g++             \
 62 |                     cmake           \
 63 |                     libgtest-dev    \
 64 |                     ninja-build     \
 65 |                     libssl-dev      \
 66 |                     clang-tidy      \
 67 |                     clang-format    \
 68 |                     libsystemd-dev
 69 | ```
 70 |
 71 |
 72 | **IMPORTANT**: building valkey-search requires GCC version 12 or higher, or Clang version 16 or higher. For Debian/Ubuntu, in case a lower version of GCC is installed, you may upgrade to gcc/g++ 12 with:
 73 |
 74 | ```sh
 75 | sudo apt update
 76 | sudo apt install -y gcc-12 g++-12
 77 | sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 1000
 78 | sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 1000
 79 | ```
 80 |
 81 | #### RedHat / CentOS / Amazon Linux
 82 |
 83 | ```sh
 84 | sudo yum update
 85 | sudo yum install -y gcc             \
 86 |                     gcc-c++         \
 87 |                     cmake           \
 88 |                     gtest           \
 89 |                     gtest-devel     \
 90 |                     ninja-build     \
 91 |                     openssl-devel   \
 92 |                     clang-tidy      \
 93 |                     clang-format    \
 94 |                     systemd-devel
 95 | ```
 96 |
 97 | ### Build the module
 98 |
 99 | valkey-search uses **CMake** for its build system. To simplify, a build script is provided. To build the module, run:
100 |
101 | ```sh
102 | ./build.sh
103 | ```
104 |
105 | To view the available arguments, use:
106 |
107 | ```sh
108 | ./build.sh --help
109 | ```
110 |
111 | Run unit tests with:
112 |
113 | ```sh
114 | ./build.sh --run-tests
115 | ```
116 |
117 | #### Integration Tests
118 |
119 | Install required dependencies (Ubuntu / Debian):
120 |
121 | ```sh
122 | sudo apt update
123 | sudo apt install -y lsb-release      \
124 |                      curl            \
125 |                      coreutils       \
126 |                      libsystemd-dev  \
127 |                      python3-pip     \
128 |                      python3.12-venv \
129 |                      locales-all     \
130 |                      locales         \
131 |                      gpg
132 |
133 | curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
134 | echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
135 | sudo apt update
136 | sudo apt-get install -y memtier-benchmark
137 | ```
138 |
139 | Run the integration tests with:
140 |
141 | ```sh
142 | ./build.sh --run-integration-tests
143 | ```
144 |
145 | ## Load the Module
146 |
147 | To start Valkey with the module, use the `--loadmodule` option:
148 |
149 | ```sh
150 | valkey-server --loadmodule /path/to/libsearch.so
151 | ```
152 |
153 | To enable JSON support, load the JSON module as well:
154 |
155 | ```sh
156 | valkey-server --loadmodule /path/to/libsearch.so --loadmodule /path/to/libjson.so
157 | ```
158 |
159 | For optimal performance, valkey-search will match the number of worker threads to the number of CPU cores on the host. You can override this with:
160 |
161 | ```sh
162 | valkey-server "--loadmodule /path/to/libsearch.so --reader-threads 64 --writer-threads 64"
163 | ```
164 |
165 | ## Development Environment
166 |
167 | For development purposes, it is recommended to use <b>VSCode</b>, which is already configured to run within a Docker container and is integrated with clang-tidy and clang-format. Follow these steps to set up your environment:
168 |
169 | 1. <b>Install VSCode Extensions:</b>
170 |     - Install the `Dev Containers` extension by Microsoft in VSCode.
171 |     - Note: Building the code may take some time, and it is important to use a host with decent CPU capacity. If you prefer, you can use a remote host. In that case, also install the following extensions:
172 |       - `Remote - SSH` by Microsoft
173 |       - `Remote Explorer` by Microsoft
174 |
175 | 2. <b>Run the dev container setup script</b>
176 |     - Issue the following command from the cloned repo root directory:
177 |         ```sh
178 |         .devcontainer/setup.sh
179 |         ```
180 |
181 | 3. <b>Open the Repository in VSCode:</b>
182 |     - On your local machine, open the root directory of the cloned valkey-search repository in VSCode.
183 |     - If the repository is located on a remote host:
184 |       1. Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS) to open the Command Palette.
185 |       2. Type Remote-SSH: Connect to Host and select it.
186 |       3. Choose the appropriate host and provide any necessary authentication details.
187 |
188 |        Once connected, VSCode will open the repository in the context of the remote host.
189 |
190 |


--------------------------------------------------------------------------------
/rfc/TEMPLATE.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | RFC: (PR number)
 3 | Status: (Change to Proposed when it's ready for review)
 4 | ---
 5 |
 6 | # Title (Required)
 7 |
 8 | ## Abstract (Required)
 9 |
10 | A few sentences describing the feature.
11 |
12 | ## Motivation (Required)
13 |
14 | What the feature solves and why the existing functionality is not enough.
15 |
16 | ## Design considerations (Required)
17 |
18 | A description of the design constraints and requirements for the proposal, along with comparisons to similar features in other projects.
19 |
20 | ## Specification (Required)
21 |
22 | A more detailed description of the feature, including the reasoning behind the design choices.
23 |
24 | ### Commands (Optional)
25 |
26 | If any new commands are introduced:
27 |
28 | 1. Command name
29 |    - **Request**
30 |    - **Response**
31 |
32 | ### Authentication and Authorization (Optional)
33 |
34 | If there are any changes around introducing new ACL command/categories for user access control.
35 |
36 | ### Append-only file (Optional)
37 |
38 | If there are any changes around the persistence mechanism of every write operation.
39 |
40 | ### RDB (Optional)
41 |
42 | If there are any changes in snapshotting mechanisms like new data type, version, etc.
43 |
44 | ### Configuration (Optional)
45 |
46 | If there are any configuration changes introduced to enable/disable/modify the behavior of the feature.
47 |
48 | ### Keyspace notifications (Optional)
49 |
50 | If there are any events to be introduced or modified to observe activity around the dataset.
51 |
52 | ### Cluster mode (Optional)
53 |
54 | If there is any special handling for this feature (e.g., client redirection, Sharded PubSub, etc) in cluster mode or if there are any new cluster bus extensions or messages introduced, list out the changes.
55 |
56 | ### Module API (Optional)
57 |
58 | If any new module APIs are needed to implement or support this feature.
59 |
60 | ### Replication (Optional)
61 |
62 | If there are any changes required in the replication mechanism between a primary and replica.
63 |
64 | ### Networking (Optional)
65 |
66 | If there are any changes introduced in the RESP protocol (RESP), client behavior, new server-client interaction mechanism (TCP, RDMA), etc.
67 |
68 | ### Dependencies (Optional)
69 |
70 | If there are any new dependency libraries required to support the feature. Existing dependencies are jemalloc, lua, etc. If the library needs to be vendored into the project, please add supporting reason for it.
71 |
72 | ### Benchmarking (Optional)
73 |
74 | If there are any benchmarks performed and preliminary results (add the hardware/software setup) are available to share or a set of scenarios identified to measure the feature's performance.
75 |
76 | ### Testing (Optional)
77 |
78 | If there are any test scenarios planned to ensure the feature's stability and validate its behavior.
79 |
80 | ### Observability (Optional)
81 |
82 | If there are any new metrics/stats to be introduced to observe behavior or measure the performance of the feature.
83 |
84 | ### Debug mechanism (Optional)
85 |
86 | If there is any debug mechanism introduced to support admin/operators for maintaining the feature.
87 |
88 | ## Appendix (Optional)
89 |
90 | Links to related material such as issues, pull requests, papers, or other references.
91 |


--------------------------------------------------------------------------------
/third_party/hdrhistogram_c/README.md:
--------------------------------------------------------------------------------
 1 | HdrHistogram_c: 'C' port of High Dynamic Range (HDR) Histogram
 2 |
 3 | HdrHistogram
 4 | ----------------------------------------------
 5 |
 6 | [![Gitter chat](https://badges.gitter.im/HdrHistogram/HdrHistogram.png)](https://gitter.im/HdrHistogram/HdrHistogram)
 7 |
 8 | Windows Build: [![AppVeyor](https://ci.appveyor.com/api/projects/status/github/HdrHistogram/HdrHistogram_c?svg=true)](https://ci.appveyor.com/project/mikeb01/hdrhistogram-c)
 9 |
10 | Linux Build: [![Build Status](https://semaphoreci.com/api/v1/mikeb01/hdrhistogram_c/branches/master/badge.svg)](https://semaphoreci.com/mikeb01/hdrhistogram_c)
11 |
12 | This port contains a subset of the functionality supported by the Java
13 | implementation.  The current supported features are:
14 |
15 | * Standard histogram with 64 bit counts (32/16 bit counts not supported)
16 | * All iterator types (all values, recorded, percentiles, linear, logarithmic)
17 | * Histogram serialisation (encoding version 1.2, decoding 1.0-1.2)
18 | * Reader/writer phaser and interval recorder
19 |
20 | Features not supported, but planned
21 |
22 | * Auto-resizing of histograms
23 |
24 | Features unlikely to be implemented
25 |
26 | * Double histograms
27 | * Atomic/Concurrent histograms
28 | * 16/32 bit histograms
29 |
30 | # Simple Tutorial
31 |
32 | ## Recording values
33 |
34 | ```C
35 | #include <hdr_histogram.h>
36 |
37 | struct hdr_histogram* histogram;
38 |
39 | // Initialise the histogram
40 | hdr_init(
41 |     1,  // Minimum value
42 |     INT64_C(3600000000),  // Maximum value
43 |     3,  // Number of significant figures
44 |     &histogram)  // Pointer to initialise
45 |
46 | // Record value
47 | hdr_record_value(
48 |     histogram,  // Histogram to record to
49 |     value)  // Value to record
50 |
51 | // Record value n times
52 | hdr_record_values(
53 |     histogram,  // Histogram to record to
54 |     value,  // Value to record
55 |     10)  // Record value 10 times
56 |
57 | // Record value with correction for co-ordinated omission.
58 | hdr_record_corrected_value(
59 |     histogram,  // Histogram to record to
60 |     value,  // Value to record
61 |     1000)  // Record with expected interval of 1000.
62 |
63 | // Print out the values of the histogram
64 | hdr_percentiles_print(
65 |     histogram,
66 |     stdout,  // File to write to
67 |     5,  // Granularity of printed values
68 |     1.0,  // Multiplier for results
69 |     CLASSIC);  // Format CLASSIC/CSV supported.
70 | ```
71 |
72 | ## More examples
73 |
74 | For more detailed examples of recording and logging results look at the
75 | [hdr_decoder](examples/hdr_decoder.c)
76 | and [hiccup](examples/hiccup.c)
77 | examples.  You can run hiccup and decoder
78 | and pipe the results of one into the other.
79 |
80 | ```
81 | $ ./examples/hiccup | ./examples/hdr_decoder
82 | ```
83 |


--------------------------------------------------------------------------------
/vmsdk/README.md:
--------------------------------------------------------------------------------
1 | # VMSDK++
2 |
3 | Valkey Module SDK++ is a C++ library that provides common functionalities for
4 | developing Valkey modules.


--------------------------------------------------------------------------------
