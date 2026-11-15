import json
from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class Step:
    key: str
    name: str
    done: bool = False
    note: str = ''

STEPS = [
    Step('validate', '验证'),
    Step('bp', 'BP'),
    Step('policy', '政策'),
    Step('pitch', '路演'),
    Step('growth', '获客'),
    Step('pricing', '定价'),
    Step('register', '注册'),
]

def progress(steps):
    done = sum(s.done for s in steps)
    return done, len(steps), round(done/len(steps)*100, 1)

def next_step(steps):
    for s in steps:
        if not s.done:
            return s
    return None

def mark(steps, key, note=''):
    for s in steps:
        if s.key == key:
            s.done = True
            s.note = note
            return True
    return False

def report(steps):
    done, total, pct = progress(steps)
    nxt = next_step(steps)
    return {
        'date': str(date.today()),
        'progress': f'{done}/{total} ({pct}%)',
        'next': nxt.name if nxt else '全部完成',
        'steps': [asdict(s) for s in steps],
    }

if __name__ == '__main__':
    mark(STEPS, 'validate', '访谈 20 位目标用户')
    mark(STEPS, 'bp', '一页纸 BP 已完成')
    print(json.dumps(report(STEPS), ensure_ascii=False, indent=2))