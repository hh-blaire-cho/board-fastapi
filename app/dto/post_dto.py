from pydantic import BaseModel, ConfigDict


class PostDto(BaseModel):
    id: int
    member_id: int
    author_name: str
    content: str
    club_id: int
    # feed_group_name: str
    # feed_group_type: FeedGroupType
    # feed_group_id: int
    # image_path: Optional[str]
    # visible: bool
    # bookmarked: bool
    # liked: bool
    # like_count: int
    # comment_count: int
    # report_count: Optional[int]
    # created_at: datetime
    # updated_at: Optional[datetime]
    # deleted_at: Optional[datetime]
    # deleted_reason: Optional[str]

    # entity → DTO 자동 변환 fromEntity 메소드 별도 구현 불필요
    model_config = ConfigDict(from_attributes=True)
