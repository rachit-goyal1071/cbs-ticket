import taipy as tp
from taipy import Config

def build_message(name: str):
    return f"Hello {name}!"


input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

hello_scenario = tp.create_scenario(scenario_cfg)
hello_scenario.input_name.write("Taipy")
hello_scenario.submit()
print(hello_scenario.message.read())
