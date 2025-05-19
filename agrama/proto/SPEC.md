## 3 · Data Model & Key Schema (Valkey)

### 3.1 Node Encoding

```protobuf
message Node {
  string uuid = 1;
  string type = 2;          // Session | Task | CodeUnit …
  int64  created_at = 3;
  int64  updated_at = 4;
  bytes  content = 5;       // protobuf-packed struct or raw bytes
  repeated float embedding = 6 [packed=true];
}
```

* **Serialization:** `buf generate` → compact varint framing; ≈ 45 B/node for metadata.

### 3.2 Key Conventions

| Purpose   | Pattern                                     | TTL  |
| --------- | ------------------------------------------- | ---- |
| Node blob | `mem:{uuid}` → `<proto bytes>`              | ∞    |
| Out edges | `mem:{src}:out:{etype}` → `[dst1 … dstN]`   | ∞    |
| In edges  | `mem:{dst}:in:{etype}`  → `[src1 … srcN]`   | ∞    |
| Temporal  | `mem:{uuid}:ts:{unix_ms}` → `<proto bytes>` | 60 d |

* Lists are **ziplist-encoded** (Valkey default) → O(1) push/pop ([GitHub][1]).
* Graph traversal: `LRANGE mem:{src}:out:*` is avoided—edge type is encoded in the key to keep look-ups O(1).
