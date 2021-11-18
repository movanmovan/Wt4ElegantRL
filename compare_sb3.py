# from stable_baselines3 import SAC as Trainer
from stable_baselines3 import TD3 as Trainer

# from stable_baselines3 import PPO as Trainer
# from stable_baselines3 import A2C as Trainer

from envs_simple_cta import SimpleCTASubProcessEnv, SimpleCTAEnv
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold
from stable_baselines3.common.monitor import Monitor
import click


@click.group()
def run():
    pass


@run.command()
def debug():
    learner = SimpleCTASubProcessEnv(**{
        'time_range': (
            # (201901011600, 202101011600),

            # (201901011600, 201906301600),
            # (201906301600, 202001011600),
            # (202001011600, 202006301600),
            # (202006301600, 202101011600),

            (201812311600, 201901311600),
            (201901311600, 201902311600),
            (201902311600, 201903311600),
            (201903311600, 201904311600),
            (201904311600, 201905311600),
            (201905311600, 201906311600),
            (201906311600, 201907311600),
            (201907311600, 201908311600),
            (201908311600, 201909311600),
            (201909311600, 201910311600),
            (201910311600, 201911311600),
            (201911311600, 201912311600),

            (201912311600, 202001311600),
            (202001311600, 202002311600),
            (202002311600, 202003311600),
            (202003311600, 202004311600),
            (202004311600, 202005311600),
            (202005311600, 202006311600),
            (202006311600, 202007311600),
            (202007311600, 202008311600),
            (202008311600, 202009311600),
            (202009311600, 202010311600),
            (202010311600, 202011311600),
            (202011311600, 202012311600),
        ),
        'slippage': 0,
        'mode': 1
    })

    evaluator = SimpleCTASubProcessEnv(**{
        'time_range': (
            # (202101011600, 202106301600),
            # (201701011600, 201706301600),
            # (201706301600, 201801011600),
            # (201801011600, 201806301600),
            # (201806301600, 201901011600),


            (202012311600, 202101311600),
            (202101311600, 202102311600),
            (202102311600, 202103311600),
            (202103311600, 202104311600),
            (202104311600, 202105311600),
            (202105311600, 202106311600),

            (201612311600, 201701311600),
            (201701311600, 201702311600),
            (201702311600, 201703311600),
            (201703311600, 201704311600),
            (201704311600, 201705311600),
            (201705311600, 201706311600),
            (201706311600, 201707311600),
            (201707311600, 201708311600),
            (201708311600, 201709311600),
            (201709311600, 201710311600),
            (201710311600, 201711311600),
            (201711311600, 201712311600),

            (201712311600, 201801311600),
            (201801311600, 201802311600),
            (201802311600, 201803311600),
            (201803311600, 201804311600),
            (201804311600, 201805311600),
            (201805311600, 201806311600),
            (201806311600, 201807311600),
            (201807311600, 201808311600),
            (201808311600, 201809311600),
            (201809311600, 201810311600),
            (201810311600, 201811311600),
            (201811311600, 201812311600),
        ),
        'slippage': 0,
        'mode': 1
    })

    env = learner

    for i in range(1):  # 模拟训练10次
        obs = env.reset()
        done = False
        n = 0
        while not done:
            action = env.action_space.sample()  # 模拟智能体产生动作
            obs, reward, done, info = env.step(action)
            n += 1
            # print('action:', action, 'obs:', obs,
            #         'reward:', reward, 'done:', done)
        print('第%s次训练完成，执行%s步, 市值%s。' % (i+1, n, env.assets))
    learner.close()


@run.command()
def train():
    learner = SimpleCTASubProcessEnv(**{
        'time_range': (
            # (201901011600, 202101011600),

            # (201901011600, 201906301600),
            # (201906301600, 202001011600),
            # (202001011600, 202006301600),
            # (202006301600, 202101011600),

            (201812311600, 201901311600),
            (201901311600, 201902311600),
            (201902311600, 201903311600),
            (201903311600, 201904311600),
            (201904311600, 201905311600),
            (201905311600, 201906311600),
            (201906311600, 201907311600),
            (201907311600, 201908311600),
            (201908311600, 201909311600),
            (201909311600, 201910311600),
            (201910311600, 201911311600),
            (201911311600, 201912311600),

            (201912311600, 202001311600),
            (202001311600, 202002311600),
            (202002311600, 202003311600),
            (202003311600, 202004311600),
            (202004311600, 202005311600),
            (202005311600, 202006311600),
            (202006311600, 202007311600),
            (202007311600, 202008311600),
            (202008311600, 202009311600),
            (202009311600, 202010311600),
            (202010311600, 202011311600),
            (202011311600, 202012311600),
        ),
        'slippage': 0,
        'mode': 1
    })

    evaluator = SimpleCTASubProcessEnv(**{
        'time_range': (
            # (202101011600, 202106301600),
            # (201701011600, 201706301600),
            # (201706301600, 201801011600),
            # (201801011600, 201806301600),
            # (201806301600, 201901011600),


            (202012311600, 202101311600),
            (202101311600, 202102311600),
            (202102311600, 202103311600),
            (202103311600, 202104311600),
            (202104311600, 202105311600),
            (202105311600, 202106311600),

            (201612311600, 201701311600),
            (201701311600, 201702311600),
            (201702311600, 201703311600),
            (201703311600, 201704311600),
            (201704311600, 201705311600),
            (201705311600, 201706311600),
            (201706311600, 201707311600),
            (201707311600, 201708311600),
            (201708311600, 201709311600),
            (201709311600, 201710311600),
            (201710311600, 201711311600),
            (201711311600, 201712311600),

            (201712311600, 201801311600),
            (201801311600, 201802311600),
            (201802311600, 201803311600),
            (201803311600, 201804311600),
            (201804311600, 201805311600),
            (201805311600, 201806311600),
            (201806311600, 201807311600),
            (201807311600, 201808311600),
            (201808311600, 201809311600),
            (201809311600, 201810311600),
            (201810311600, 201811311600),
            (201811311600, 201812311600),
        ),
        'slippage': 0,
        'mode': 2
    })

    n = 1500

    eval_callback = EvalCallback(
        eval_env=Monitor(evaluator),
        callback_on_new_best=StopTrainingOnRewardThreshold(
            reward_threshold=5, verbose=1),
        n_eval_episodes=30,
        eval_freq=24,
        log_path='./outputs_bt/sb3/%s'%Trainer.__name__,
        best_model_save_path='./outputs_bt/sb3/%s'%Trainer.__name__,
        verbose=1)

    model: Trainer = Trainer('MlpPolicy', learner,
                             #  gamma=0.1 ** (1/12/8),
                             gamma=0.96,
                             #  learning_rate=2 ** -14,  # 15: 167, 14:
                             learning_rate=1e-5,
                             # learning_starts=100,
                             # batch_size=128,
                            #  ent_coef='auto_0.1',
                             # policy_kwargs=dict(net_arch=[128, 128, 128]),
                             tensorboard_log='./outputs_bt/sb3/%s'%Trainer.__name__,
                             verbose=1,
                             #  device='cpu',
                             )
    model.learn(
        total_timesteps=10000,
        callback=eval_callback,
        log_interval=1
    )
    model.save('SimpleTrainer')


@run.command()
@click.option('--path', '-p', 'path')
def test(path):
    env = SimpleCTAEnv(**{
        # 'time_start': 201701011600,
        # 'time_end': 201901011600,
        # 'time_start': 202001011600,
        # 'time_end': 202108311600,
        'time_start': 202108311600,
        'time_end': 202110131600,
        # 'time_end': 202110281600,
        'slippage': 0,
        'mode': 2,
        'id': 2,
    })
    model = Trainer.load(path)

    for i in range(1):  # 模拟训练10次
        obs = env.reset()
        done = False
        n = 0
        while not done:
            action = model.predict(obs)[0]
            obs, reward, done, info = env.step(action)
            n += 1
            # print(
            #     # 'action:', action,
            #     # 'obs:', obs,
            #     'reward:', reward,
            #     # 'done:', done
            #     )
        #     break
        # break
        print('第%s次测试完成，执行%s步, 市值%s。' % (i+1, n, env.assets))
    env.close()


if __name__ == '__main__':
    run()
