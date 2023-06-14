def conf_prep(a, b, c, d, **kwargs):
    trigger_conf = kwargs["dag_run"].conf
    print(trigger_conf)
    print("hi", a, b, c, d)
