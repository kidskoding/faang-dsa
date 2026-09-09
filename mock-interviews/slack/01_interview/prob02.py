class ReplyNode:
    def __init__(
        self,
        id: int = 0,
        earlier: "ReplyNode | None" = None,
        later: "ReplyNode | None" = None,
    ) -> None:
        self.id = id
        self.earlier = earlier
        self.later = later


def prob02(root: ReplyNode | None) -> list[int]:
    pass
