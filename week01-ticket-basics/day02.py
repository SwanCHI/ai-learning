def count_status(tickets: list[dict]) -> dict[str: int]:
    """
        统计ticket 每种状态数量

        param : tickets: list[{},{},]
        return: dict{}
    """
    # if tickets == None or len(tickets) == 0:
    #     return {}
    
    stat_count = {}
    for ticket in tickets:
        status = ticket.get('status')
        stat_count[status] = stat_count.get(status, 0) + 1
    return stat_count


def get_open_ids(tickets: list[dict]) -> list[int]:
    """
        返回未关闭工单编号

    """
    # if tickets == None or len(tickets) == 0:
    #     return []
    
    filter_tickets = [ticket for ticket in tickets if ticket.get("status") == "open"]
    filter_tickets = sorted(filter_tickets, key = lambda t : (t["priority"], t["id"]))
    return [t["id"] for t in filter_tickets]

tickets = [
  {"id":"T002","title":"邮箱密码重置","category":"account","priority":2,"status":"closed"},
  {"id":"T003","title":"申请安装开发工具","category":"software","priority":3,"status":"open"},
  {"id":"T004","title":"账号被锁定","category":"account","priority":1,"status":"open"},
  {"id":"T001","title":"VPN无法连接","category":"network","priority":1,"status":"open"},
]


# status_count = count_status(tickets=tickets)
# print(f"status_count: {status_count}")

# ids = get_open_ids(tickets=tickets)
# print(f"ids = {ids}")

# count_status(1)

assert count_status(tickets) == {"open": 3, "closed": 1}
assert get_open_ids(tickets) == ["T001", "T004", "T003"]

assert count_status([]) == {}
assert get_open_ids([]) == []
assert [t["id"] for t in tickets] == ["T002", "T003", "T004", "T001", ]
print(count_status(tickets))
print(get_open_ids(tickets))
    
