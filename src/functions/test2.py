from task2 import get_sorted_report


lists = [
    [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55}
    ],
    [ 
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00}
    ],
    [
        {"category": "Drama", "total_sales": 500.00}
    ]
]

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
for dict_list in lists:
    dict_list = get_sorted_report(dict_list)
    print("Топ категорий по выручке:")
    
    i = 1
    for d in dict_list:
        print(f"{i}. {d['category']}: {d['total_sales']}")
        i += 1
    print()
