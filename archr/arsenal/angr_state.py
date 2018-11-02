import logging

l = logging.getLogger("archr.arsenal.angr_state")

from . import Bow

class angrStateBow(Bow):
    """
    Describes a target in the form of a Docker image.
    """

    def __init__(self, target, project_bow):
        super(angrStateBow, self).__init__(target)
        self.project_bow = project_bow
        self.target.mount_local()

    def fire(self, **kwargs): #pylint:disable=arguments-differ
        project = self.project_bow.fire()
        s = project.factory.full_init_state(
            concrete_fs=True, chroot=self.target.local_path,
            stack_end=self.project_bow._mem_mapping['[stack-end]'], args=self.target.target_args, env=self.target.target_env,
            brk=self.project_bow._mem_mapping['[heap]'],
            **kwargs
        )
        return s