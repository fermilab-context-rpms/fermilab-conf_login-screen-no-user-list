_default:
	@echo "make"
sources:
	@echo "make sources"
	@tar cvf - conf | xz > fermilab-conf_login-screen-no-user-list.tar.xz
srpm: sources
	@echo "make srpm"
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' fermilab-conf_login-screen-no-user-list.spec
