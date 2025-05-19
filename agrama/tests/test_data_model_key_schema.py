from hypothesis import given, strategies as st

from agrama.proto.node_pb2 import Node
from agrama.db.schema import new_uuid, make_node_key, parse_node_key


@given(node_type=st.sampled_from(["Session", "Task", "CodeUnit"]))
def test_key_schema_roundtrip(node_type: str) -> None:
    uuid = new_uuid()
    key = make_node_key(uuid, node_type)
    assert parse_node_key(key) == (uuid, node_type)


def test_node_serialization_roundtrip() -> None:
    node = Node(
        uuid="abc123",
        type="Session",
        created_at=123456789,
        updated_at=123456790,
        content=b"data",
        embedding=[1.0, 2.0, 3.0],
    )
    data = node.SerializeToString()
    node2 = Node()
    node2.ParseFromString(data)
    assert node == node2
