import click
@click.command()
@click.option("--happy",default=1,help="程序员节日快乐.")
def run(happy):
    """这是一个简单的运行命令."""
    for _ in range(happy):
        click.echo("1024,程序员节日快乐")
        if __name__=='__main__':
            run()